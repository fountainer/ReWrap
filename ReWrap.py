import sublime, sublime_plugin, re

class ReWrapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region_set = self.view.sel()[0]
        region_text = self.view.substr(region_set )
        settings = sublime.load_settings('ReWrap.sublime-settings')
        width = settings.get("width", 120)
        region_text = re_format(region_text, width)
        self.view.replace(edit, region_set, region_text)


# a string or a list of string? see sumblime text api
def re_format(s, width):
    s = re.sub("\n+", " ", s)
    s = re.sub("\s+", " ", s)
    s = s.split()
    s.reverse()
    s_res = []
    while (len(s) > 0):
        length = len(s[-1])
        s_tmp = []
        while (length <= width):
            s_tmp.append(s.pop())
            if (len(s) > 0):
                length = length + len(s[-1]) + 1
            else:
                length = width + 1
        s_res.append(s_tmp)
    s_res = [" ".join(substr) for substr in s_res]
    s_res = "\n".join(s_res)
    s_res = s_res + "\n"
    return s_res