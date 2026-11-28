# Pictures on the screen

Say **"show me a dog"** or **"show me a cat"**: the skill asks a free web
service for a random picture and shows it on the device's screen – in all
twelve of [Emkay](https://emkay.ai)'s languages. A device without a screen
still hears the answer.

**👉 The friendly guide: <https://dev.emkay.ai>**

## What it shows

- **The screen:** `self.gui.show_image(url, title=..., fill=...)` shows a
  picture. `self.gui` can also show text (`show_text`), a web page
  (`show_url`) or your own page – see the
  [OVOS GUI docs](https://openvoiceos.github.io/ovos-technical-manual/gui/).
- **Asking the web:** two free services, no account or key –
  [dog.ceo](https://dog.ceo/dog-api/) and [The Cat API](https://thecatapi.com/).
  Emkay's *What's happening?* view shows each call.
- **One handler, two intents:** `dog.intent` and `cat.intent` both end in
  `show()`; the dialogs are named after the animal (`dog_here.dialog`,
  `cat_here.dialog`).
- **Text from a dialog without speaking it:**
  `self.dialog_renderer.render("dog_title")` – the title on the screen.

## Try changing

- `FILL` – `PreserveAspectCrop` fills the whole screen;
- `SHOW_FOR` – how many seconds the picture stays before the clock comes back;
- show text instead: `self.gui.show_text("Hello!")`;
- a third animal: a new intent, two dialogs, and a free picture service.

## A working skill, and a template

This is a complete OpenVoiceOS skill – install it and it works – and an
example to start your own from: *Use this template* on GitHub, or
*Emkay: New skill* in VS Code ([Emkay Code](https://dev.emkay.ai)), which
gives it your own names. Made for [Emkay](https://emkay.ai), it runs on any
OpenVoiceOS.

## Try it

- **Emkay Code (VS Code):** *Emkay: Run the skill in Emkay* (Ctrl+Alt+E) opens
  Emkay next to your code and loads the skill; type under Emkay to talk to it.
  Every save loads it again. *Emkay: Test the skill* sends the golden
  utterances and shows ✓ / ✗ in the Testing view. Emkay's menu →
  *Guardian* → *What's happening?* shows which skill took a sentence, and why.
- **ovos-tui-client (Codespaces, Dev Container):** run `ovos-tui` in the
  terminal, type to talk, `Ctrl+P` → *Test* runs the same golden utterances
  against a full OpenVoiceOS.
- **pytest:** `pytest -q` – no OpenVoiceOS needed.

When you make a repository from this template ("Use this template"), a
small workflow renames the skill after your repository and then removes
itself.

## Show it, on your own Emkay, and into the store

To show it in [See my skill](https://dev.emkay.ai/#gallery) on dev.emkay.ai –
ready or not – add the topic `emkay-skill` to the repository (the ⚙ next to
*About*). Remove the topic, or make the repository private, to take it away.

*Emkay: Send to my Emkay* shows a QR code that installs this skill from
GitHub on the Emkay you scan it with. To get it into the
[Emkay store](https://store.emkay.ai): topics `ovos` and `openvoiceos` on the
repository, a release on GitHub (`publish.yml` puts it on PyPI), and the
store's nightly test does the rest – <https://dev.emkay.ai/#store>.

More on writing skills:
[the OpenVoiceOS technical manual](https://openvoiceos.github.io/ovos-technical-manual/).
