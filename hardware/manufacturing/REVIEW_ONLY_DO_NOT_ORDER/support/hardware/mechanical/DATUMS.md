# Coordinate frames for the proposed 330 x121.5 outline

Updated 2026-10-09. Root proposes extending only the rear edge from native y20 to y18.5, keeping x20..350/y140 front and every native placement fixed. No helper native mutation or readback of the proposed new edge is claimed. The socket correction evidence is in [SOCKET_EDGE_REVIEW.md](SOCKET_EDGE_REVIEW.md).

**Legacy mechanical frame:** native = local+(20,20), x right/y toward front. Existing fixture/socket/cassette CSVs, DXFs and SVG element coordinates retain this frame for stable interface references. The proposed board outline is local x0..330/y-1.5..120.

This is the retained service/fixture datum requested by root. The actual proposed physical upper-left is native (20,18.5); it is not the retained service origin at (20,20).

**Optional physical top-left frame:** if a future document explicitly adopts the new y18.5 outline's top-left origin, native = local+(20,18.5). Its board outline is x0..330/y0..121.5. Convert `x_new=x_legacy`, `y_new=y_legacy+1.5`. This is only a coordinate-label conversion; the current mechanical interfaces retain the legacy frame. Do not use a legacy y with the new +18.5 offset: that would move the component 1.5 mm rearward.

| Reference | Legacy local (+20,+20) | New outline local (+20,+18.5) | Native, unchanged |
|---|---|---|---|
| Rear-left proposed corner | (0,-1.5) | (0,0) | (20,18.5) |
| Front-right corner | (330,120) | (330,121.5) | (350,140) |
| J1 pad1 | (111.11,1.30) | (111.11,2.80) | (131.11,21.30) |
| J2 pad1 | (128.89,49.56) | (128.89,51.06) | (148.89,69.56) |
| Pico PCB rear-left | (109.5,0) | (109.5,1.5) | (129.5,20) |
| Cassette minimum | (145,12) | (145,13.5) | (165,32) |
| Cassette maximum | (257,48) | (257,49.5) | (277,68) |
| Cassette mount 1 | (150,17) | (150,18.5) | (170,37) |
| Cassette mount 2 | (210,17) | (210,18.5) | (230,37) |
| Cassette mount 3 | (150,43) | (150,44.5) | (170,63) |
| Cassette mount 4 | (210,43) | (210,44.5) | (230,63) |
| Holder platform hole 1, nominal | (172.83,30) | (172.83,31.5) | (192.83,50), cassette-only reference |
| Holder platform hole 2, nominal | (228.44,30) | (228.44,31.5) | (248.44,50), cassette-only reference |
| H1 pad1, root 806457b held export | (269,20) | (269,21.5) | (289,40) |
| Semitone modifier centre | (24,54) | (24,55.5) | (44,74) |
| Octave modifier centre | (24,94) | (24,95.5) | (44,114) |
| Note body centres C4..C5 | x70+34n, y94 | x70+34n, y95.5 | x90+34n, y114 |
| Fixture rear/front bounds | y36..119 | y37.5..120.5 | y56..139 |

Nominal holder hole references are not new carrier holes; exact-part mounting tolerance/fasteners remain pending. The proposed extra 1.5 mm does not affect row pitch, key spacing, support height, cassette dimensions or z datums. z for upper fixture is up from carrier top; z for cassette is down from underside.

The updated paper SVG is **330 mm wide x121.5 mm high**, viewBox `0 -1.5 330 121.5`; its original geometric coordinates are preserved. The current `print_paper_fit.py` accepts that viewBox/depth and maps legacy y through `y+1.5` into the printed top-left frame, including labels and alignment coordinates. Both pages of the [revised Letter paper-fit PDF](../../output/pdf/make-music-paper-fit-letter.pdf) have been rendered and inspected. Print at 100% actual size and verify the scale bars; this is a comfort/spacing reference, not proof of physical part fit.

For root's absolute native x-right/y-up exports, use (20,-18.5)..(350,-140) with all component export positions unchanged. Older auxiliary-bottom-left exports use another origin and remain obsolete; do not add 1 to their arbitrary coordinates or mix manifests.
