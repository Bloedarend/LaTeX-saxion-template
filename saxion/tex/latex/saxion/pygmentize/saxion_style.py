from pygments.style import Style
from pygments.token import *

# Saxion brand palette with semantic color names
primary     = "#01826d"
secondary   = "#1565c0"
tertiary    = "#0090d9"
accent      = "#FF7043"
text        = "#37474F"
comment     = "#6E7B8B"
background  = "#F5F7FA"
highlight   = "#80CBC4"
white       = "#FFFFFF"

class SaxionStyle(Style):
    background_color = background
    default_style = ""

    styles = {
        Text:                  text,
        Whitespace:            "",

        Error:                 f"border:{accent}",

        Comment:               comment,
        Comment.Multiline:     comment,
        Comment.Preproc:       comment,
        Comment.Single:        comment,
        Comment.Special:       comment,

        Keyword:               f"bold {primary}",
        Keyword.Constant:      f"bold {primary}",
        Keyword.Declaration:   f"bold {primary}",
        Keyword.Namespace:     f"bold {primary}",
        Keyword.Pseudo:        f"bold {primary}",
        Keyword.Reserved:      f"bold {primary}",
        Keyword.Type:          f"bold {primary}",

        Name:                  text,
        Name.Attribute:        tertiary,
        Name.Builtin:          primary,
        Name.Builtin.Pseudo:   primary,
        Name.Class:            tertiary,
        Name.Constant:         tertiary,
        Name.Decorator:        accent,
        Name.Entity:           text,
        Name.Exception:        accent,
        Name.Function:         tertiary,
        Name.Label:            text,
        Name.Namespace:        text,
        Name.Other:            text,
        Name.Tag:              primary,
        Name.Variable:         text,
        Name.Variable.Class:   text,
        Name.Variable.Global:  text,
        Name.Variable.Instance:text,

        Literal:               highlight,
        Literal.Date:          primary,

        String:                secondary,
        String.Backtick:       secondary,
        String.Char:           secondary,
        String.Doc:            secondary,
        String.Double:         secondary,
        String.Escape:         secondary,
        String.Heredoc:        secondary,
        String.Interpol:       secondary,
        String.Other:          secondary,
        String.Regex:          secondary,
        String.Single:         secondary,
        String.Symbol:         secondary,

        Number:                tertiary,
        Number.Bin:            tertiary,
        Number.Float:          tertiary,
        Number.Hex:            tertiary,
        Number.Integer:        tertiary,
        Number.Integer.Long:   tertiary,
        Number.Oct:            tertiary,

        Operator:              secondary,
        Operator.Word:         f"bold {secondary}",

        Punctuation:           text,

        Generic:               text,
        Generic.Deleted:       accent,
        Generic.Error:         f"border:{accent}",
        Generic.Heading:       f"bold {text}",
        Generic.Inserted:      highlight,
        Generic.Output:        comment,
        Generic.Prompt:        comment,
        Generic.Strong:        "bold",
        Generic.Subheading:    f"bold {text}",
        Generic.Traceback:     f"border:{accent}",
    }
