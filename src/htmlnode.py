


class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list[object] | None = None, 
            props: dict[str, str] | None = None
        ):
            self.tag = tag
            self.value = value
            self.children = children
            self.props = props


    def to_html(self):
         raise NotImplemented



    def props_to_html(self):
         if self.props is None or self.props == {}:
            return ""
         result = ""
         for key, value in self.props.items():
              result += f' "{key}"="{value}"'
         return result


    def __eq__(self, other):
            if not isinstance(other, HTMLNode):
                return NotImplemented
            return (
                self.tag,
                self.value,
                self.children,
                self.props
            ) == (
                other.tag,
                other.value,
                other.children,
                other.props
            )


    def __repr__(self):
         return (
               f"HTMLNode("
               f"tag={self.tag!r}, "
               f"value={self.value!r}, "
               f"children={self.children!r}, "
               f"props={self.props!r})"
        )