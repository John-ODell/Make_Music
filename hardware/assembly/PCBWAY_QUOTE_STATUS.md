# PCBWay conditional quote status

## October 19 cable drawing response

PCBWay acknowledged the files and requested a cable drawing. A warm reply to
Grace supplied the three-page cable PDF as an actual attachment; Gmail SENT
readback confirms its filename, application/pdf type and 8955 bytes. See
[cable drawings](../../output/pdf/MakeMusic_Cable_Drawings_RevA_QUOTE_ONLY.pdf).
Each sheet was rendered/visually inspected and its mapping/quantities checked
against the prior wire specification. Existing ZIP/programming/BOM/CAD unchanged.

The attachment defines logical circuits, wire/contact specifications and initial
allowances. It explicitly does not establish physical connector views or final
fitted lengths. The email asks the supplier to return actual module revisions,
module-end mating-face/wire-entry views and final dressed lengths for review.
These are quoted engineering/metrology inputs, still held under issue44.
No purchase, cable manufacture, carrier fabrication or assembly release.

## October 18 actual-attachment delivery

Grace could not open the previously sent links and requested attachments.
A user-authorized, thankful reply was sent through Gmail with five actual
attachments: wire specification, programming instructions and test procedure
as .txt files, the complete factory-input ZIP (including main.py and runtime
UF2), and the unchanged grouped carrier BOM XLSX. The SENT message was read
back and all five MIME filenames/types/sizes confirmed. The text files and
ZIP contents match the reviewed inputs; no design/firmware changes were made.

This transmission used the working Gmail connector; browser attachment
permission remains unchanged. Private receipts remain local. Supplier receipt,
acceptance and the revised quote are pending. Delivery remains two complete
instruments plus three populated carriers, five total; production holds and
quote-only status remain unchanged. See issue49 for the receipt update.

## October 16 factory-input response

The supplier confirmed the requested split and asked for wire specification,
programming file and test file. A cordial, user-authorized reply was sent to
Grace in the same quotation thread at 9:23 a.m. America/Chicago; Gmail confirmed
sending. It supplied separate document links and a direct ten-file ZIP download
pinned to afe55c4f9db64f1afb34ae8138d98cb3b9cbe795; see
[factory handoff](factory-handoff/README.md). The ZIP includes the unchanged
application, official stable RP2040 MicroPython runtime, wiring/programming/test
procedures, source/license and checksums. No attachment was uploaded because
local browser upload permission is disabled; no permission was changed.

Seven host checks and 32 documented note/modifier cases pass on the computer.
No real Pico/runtime, module, mechanical or power test is claimed. Exact module
fit/ends/cut lengths, touch polarity, final mechanics, cell/charger and physical
acceptance remain held; tracked in GitHub issue44. Await the supplier's revised
price/capability/engineering response. No order or production release.

## October 15 update

The user completed the website upload on October 10, then supplied the
grouped replacement BOM prepared in PR39. PCBWay has returned a quotation
of $326.65 for five populated carriers: $199.85 parts, $29 assembly and
$97.80 PCBs. Shipping/tax and completion of instruments are not established
by that price. The returned 19 BOM groups match all 47 carrier parts per board.

The user now requests **two complete instruments and three populated carriers**,
with generic touch/passive-buzzer modules permitted as engineering candidates.
The [revised scope and retail references](REVISED_QUOTE_2_COMPLETE_3_CARRIERS.md)
were sent by email at the user's explicit instruction on October 15 at
8:32 a.m. America/Chicago. Gmail confirmed sending in the existing quotation
thread. The cordial reply supplied exact revision-pinned links to the XLSX BOM
and revised request at fb8d1dae1861da73a01eb0fe8ad9ecf3521c0871. Local attachment
upload was blocked by Chrome permission and the Gmail connector was rate-limited;
no attachment was transmitted and no permission was changed. Supplier acceptance
and revised complete-instrument pricing remain pending. The prior
five-complete-instrument preference below is historical.
No fabrication, payment or production release is authorized.

## Historical October 9 transmission record

Prepared October 9, 2026. **Quotation only; no fabrication or purchase release.**
The owner authorized a final team review and PCBWay quotation submission.
[Final review](../review/prequote-20261009/README.md) accepts conditional pricing.

Requested alternative scopes for the same physical design:

- A: five bare carriers.
- B: five carriers with all47 purchased parts each supplied and soldered,
  including all30 SMT and17 THT parts.
- C: five complete instruments, including engineering/metrology, final
  mechanical work, harnesses, programming and tests. This is the preferred scope.
- Optional additional sixth bare keepsake, separately priced.

These alternatives do not authorize an order for fifteen boards. Exact-part
fit, cell/charger qualification, final mechanics, process acceptance and tests
remain held; see [full quote request](QUOTE_REQUEST.md).

## Current transmission state

**SENT and confirmed in PCBWay Message History on October9,2026 at8:40:22 p.m.
America/Chicago** (site displays October10,09:40:22 China time). The1759-character
RFQ went once to the account's assigned representative, Cici. Email reply was
selected. An itemized A/B/C quotation is pending; receipt does not establish that
the representative has read or accepted the engineering scope.

The signed-in online assembly form produced an indicative estimate but did not
save a cart entry. No cart-based submission or order number exists. The message
center was used instead. Browser file upload required a permission not enabled;
no attachment was uploaded. The RFQ supplied exact revision-pinned public links
to the reviewed packet and repository ZIP, with instructions to use only
`hardware/manufacturing/REVIEW_ONLY_DO_NOT_ORDER`:

- [Exact reviewed packet](https://github.com/John-ODell/Make_Music/tree/0d6191a0e0217e7140bbceed22aa4e59db78747e/hardware/manufacturing/REVIEW_ONLY_DO_NOT_ORDER)
- [Exact revision download](https://github.com/John-ODell/Make_Music/archive/0d6191a0e0217e7140bbceed22aa4e59db78747e.zip)

The packet was pushed and integrated through
[PR37](https://github.com/John-ODell/Make_Music/pull/37), merge
bc986a28121235c059e4859eb6203bb539a0c00a. GitHub's content API confirmed the
specified committed packet directory exists. Native CAD and exports unchanged.
The sent-message screenshot and exact RFQ text are local operational records
in `output/pcbway-quote-20261009/`; no account/session data is committed here.
Chrome permissions need not be changed for this completed link-based RFQ.

No payment, fabrication, first-article build or production release was approved.

The web calculator showed $97.80 PCB fabrication, $29 assembly service,
$40.28 estimated US/DHL shipping and a $30 promotion, yielding $137.08.
This excludes component purchasing, custom services/engineering and duties/tax;
it is **not the price of five complete instruments** and is subject to review.

## Exact prepared attachments — not transmitted

Both files are in `output/pcbway-quote-20261009/`. Each is below the message
center's1MB limit. Extract both into one folder; their disjoint contents cover
the109 hashed outputs plus manifest. Every decompressed payload matches the
reviewed full packet byte-for-byte.

| File | Bytes | Files | SHA256 |
|---|---:|---:|---|
| MakeMusic_Quote_Core_DO_NOT_FABRICATE.zip |959587|33|4a7e79b52dc5717e9446ccdbbf5e90967dc73be3662cd751dabbb3b1a34e3024|
| MakeMusic_Quote_Support_DO_NOT_FABRICATE.zip |225854|77|b9ba53f1cb3e2ab6bf4c8f4b2a81bf21e95f29bd9661d178598f0ce208df94a9|

No credentials, account identifiers or personal contact details belong in this
public repository. Browser receipts/screenshots remain local operational files.
