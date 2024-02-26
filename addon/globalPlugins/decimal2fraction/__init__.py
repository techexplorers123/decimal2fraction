import ui
import scriptHandler
import textInfos
import addonHandler 
from globalPluginHandler import GlobalPlugin
import api

addonHandler.initTranslation()

class GlobalPlugin(GlobalPlugin):
    scriptCategory = _("decimal to fraction")
    def __init__(self):
        super(GlobalPlugin, self).__init__()

    @scriptHandler.script(
        description=_("converts the coppyed decimal to fraction"),
        gesture="kb:nvda+alt+a"
    )
    def script_clipFraction(self, gesture):
        clipboard_data = api.getClipData()
        if clipboard_data:
            num = float(clipboard_data)
            result = self.float_to_fraction(num)
            if scriptHandler.getLastScriptRepeatCount() == 0:
                ui.message(result)
            else:
                api.copyToClip(result, notify=True)
        else:
            ui.message(_("Error: Clipboard is empty"))

    def getSelectedText(self):
        obj=api.getCaretObject()
        try:
            info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
            if info or not info.isCollapsed:
                return info.text
        except (RuntimeError, NotImplementedError):
            return None

    @scriptHandler.script(
        description=_("converts the selected text to a fraction"),
        gesture="kb:nvda+alt+s"
    )
    def script_convertSelection(self, gesture):
        num = self.getSelectedText()
        if not num:
            ui.message(_("no selection"))
        else:
            result = self.float_to_fraction(float(num))
            if scriptHandler.getLastScriptRepeatCount() == 0:
                ui.message(result)
            else:
                api.copyToClip(result, notify=True)

    def float_to_fraction(self, num):
        tolerance = 1.0e-9
        h1, h2 = 1, 0
        k1, k2 = 0, 1
        b = num
        while True:
            a = int(b)
            h1, h2 = a * h1 + h2, h1
            k1, k2 = a * k1 + k2, k1
            b = 1 / (b - a) if (b - a) != 0 else float('inf')
            if abs(num - h1 / k1) < num * tolerance:
                return f"{h1}/{k1}"
