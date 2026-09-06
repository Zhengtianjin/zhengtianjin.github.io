#!/usr/bin/env python3
"""Refresh Scholar's author total and publication counts without damaging the cache."""
import os
from pathlib import Path
from datetime import datetime, timezone
import yaml
from scholarly import scholarly


def get_scholar_citations():
    config = yaml.safe_load(Path('_data/socials.yml').read_text()) or {}
    user_id = config.get('scholar_userid')
    if not user_id:
        raise ValueError('Missing scholar_userid in _data/socials.yml')
    scholarly.set_timeout(20)
    scholarly.set_retries(2)
    author = scholarly.fill(scholarly.search_author_id(user_id), sections=['basics', 'indices', 'publications'])
    if author.get('scholar_id') != user_id or 'citedby' not in author or 'publications' not in author:
        raise ValueError('Incomplete Scholar response; existing cache retained')
    total = author['citedby']
    if not isinstance(total, int) or total < 0:
        raise ValueError('Invalid author citation total; existing cache retained')
    data = {
        'metadata': {'last_updated': datetime.now(timezone.utc).strftime('%Y-%m-%d')},
        'author': {'scholar_id': user_id, 'total_citations': total},
        'papers': {},
    }
    for pub in author['publications']:
        pub_id = pub.get('author_pub_id') or pub.get('pub_id')
        count = pub.get('num_citations')
        title = pub.get('bib', {}).get('title')
        if not pub_id or not title or not isinstance(count, int) or count < 0:
            raise ValueError('Incomplete publication data; existing cache retained')
        if ':' not in pub_id:
            pub_id = f'{user_id}:{pub_id}'
        if not pub_id.startswith(f'{user_id}:'):
            raise ValueError('Publication belongs to a different author')
        data['papers'][pub_id] = {'title': title, 'year': str(pub.get('bib', {}).get('pub_year', '')), 'citations': count}
    if total > 0 and not data['papers']:
        raise ValueError('Missing publication list; existing cache retained')
    output = Path('_data/citations.yml')
    temporary = output.with_suffix('.yml.tmp')
    try:
        temporary.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding='utf-8')
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Synced {len(data['papers'])} papers; author total: {total}")


if __name__ == '__main__':
    get_scholar_citations()
