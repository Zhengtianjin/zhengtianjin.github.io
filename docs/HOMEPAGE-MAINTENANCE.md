# Homepage research content

The existing al-folio / GitHub Pages build is retained. The homepage uses `_pages/about.html` with its own compact, light academic design; other pages retain their existing layouts.

- `_data/home_news.yml`: your homepage news, newest dates first. Five recent entries appear immediately; older entries expand on the same page. Add only your own verified news.
- `_data/home_papers.yml`: homepage paper presentation, authors, venue, links, optional video/poster/PDF and exact Google Scholar publication ID. Keep formal bibliographic records in `_bibliography/papers.bib` consistent with this presentation list.
- `assets/video/trace.mp4`: official TRACE demonstration, hosted locally to avoid GitHub's expiring signed video URLs. Source: https://github.com/spikelab-jhu/trace-active-reconstruction#-video (retrieved 2026-09-06 UTC).
- `assets/img/trace-video-poster.jpg`: still from that video. Video playback is muted initially, user-controlled, inline, and does not automatically download the full video on page load.
- `assets/pdf/trace.pdf` and `assets/pdf/ergodic.pdf`: public arXiv PDFs retrieved from https://arxiv.org/pdf/2608.02304 and https://arxiv.org/pdf/2512.08661. The browser reader is created only after expanding a paper. A new-tab fallback remains available. Other papers retain publisher/Scholar links until a shareable PDF is supplied.

## Citations

Run `python bin/update_scholar_citations.py` from the repository root with `scholarly` and `PyYAML` installed. It updates `_data/citations.yml`; a site rebuild/deployment is needed to show changes publicly.

The author total comes directly from Google Scholar's author-level `citedby` field. Each paper is mapped using `scholar_id`; missing counts are not displayed as zero. A failed/incomplete fetch leaves the previous cache intact and exits with an error. The homepage shows the last successful UTC sync date. This is cached synchronization, not a real-time request from every visitor's browser. Google Scholar may throttle automated requests.

News and paper records are curated, not automatically inferred from other researchers' websites or Scholar. Saving and deploying these data files refreshes the homepage.

The existing scheduled workflow has not been changed in this revision pending explicit approval for automatic commits and deployment.

## Validation

- Jekyll production generation completed locally.
- Starter style contract passed; no plugin-owned files are overridden.
- Four cache tests cover first run, author total vs. sum, zero counts, and preserving data on partial/network failures.
- Browser checks verified four paper entries, TRACE playback, an expandable PDF reader, and no horizontal overflow at 390px.
