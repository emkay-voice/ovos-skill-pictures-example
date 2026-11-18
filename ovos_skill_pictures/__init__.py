"""Pictures on the screen: say "show me a dog" or "show me a cat".

The skill asks a free web service for a random picture (no account, no key)
and shows it on the device's screen with self.gui.show_image(). A device
without a screen still hears the answer.

  dogs: https://dog.ceo/dog-api/
  cats: https://thecatapi.com/

Try changing: the title shown with the picture (dog_title.dialog), how the
picture fills the screen (FILL), or show text instead with
self.gui.show_text("Hello!").
"""
import requests

from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill

DOG_API = "https://dog.ceo/api/breeds/image/random"
CAT_API = "https://api.thecatapi.com/v1/images/search"
FILL = "PreserveAspectFit"   # the whole picture; "PreserveAspectCrop" fills the screen


class PicturesSkill(OVOSSkill):

    def picture(self, kind):
        """The address of a random picture of a dog or a cat, or None."""
        try:
            if kind == "dog":
                return requests.get(DOG_API, timeout=10).json()["message"]
            return requests.get(CAT_API, timeout=10).json()[0]["url"]
        except Exception as e:
            self.log.warning(f"no {kind} picture: {e}")
            return None

    def show(self, kind):
        url = self.picture(kind)
        if not url:
            self.speak_dialog("no_picture")
            return
        self.gui.show_image(url, title=self.dialog_renderer.render(f"{kind}_title"), fill=FILL)
        self.speak_dialog(f"{kind}_here")

    @intent_handler("dog.intent")
    def handle_dog(self, message):
        self.show("dog")

    @intent_handler("cat.intent")
    def handle_cat(self, message):
        self.show("cat")
