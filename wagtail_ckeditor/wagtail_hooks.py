from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.admin.rich_text.converters.editor_html import WhitelistRule
from wagtail.core import hooks
from wagtail.core.whitelist import allow_without_attributes, attribute_rule

# from wagtail_ckeditor import settings


@hooks.register("insert_editor_js")
def ckeditorjs():
    return format_html(
        '<script src="{src}"></script>',
        src=static("ckeditor/ckeditor.js"),
    )


@hooks.register("register_rich_text_features")
def apply_whitelist(features):
    features.register_converter_rule(
        "editorhtml",
        "ckeditor_features",
        [
            WhitelistRule("s", allow_without_attributes),
            WhitelistRule("u", allow_without_attributes),
            WhitelistRule("span", attribute_rule({"style": True, "class": True})),
            WhitelistRule("p", attribute_rule({"style": True, "class": True})),
            WhitelistRule("div", attribute_rule({"style": True, "class": True})),
            WhitelistRule("q", allow_without_attributes),
            WhitelistRule("ins", allow_without_attributes),
            WhitelistRule("pre", allow_without_attributes),
            WhitelistRule("addres", allow_without_attributes),
            WhitelistRule(
                "div",
                attribute_rule(
                    {
                        "align": True,
                        "border": True,
                        "cellpadding": True,
                        "style": True,
                    }
                ),
            ),
            WhitelistRule("caption", allow_without_attributes),
            WhitelistRule("thead", allow_without_attributes),
            WhitelistRule("tr", allow_without_attributes),
            WhitelistRule("tbody", allow_without_attributes),
            WhitelistRule("td", attribute_rule({"style": True, "class": True})),
            WhitelistRule("hr", allow_without_attributes),
            WhitelistRule(
                "img",
                attribute_rule(
                    {
                        "alt": True,
                        "src": True,
                        "style": True,
                        "width": True,
                        "height": True,
                    }
                ),
            ),
        ],
    )
    features.default_features.append("ckeditor_features")
