

class HTMLNode:



    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props = ''
        for key, value in self.props.items():
            props += f' {key}="{value}"'

        return props 

        
    def __repr__(self):

        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        



class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid html: node requires a tag")
        if self.children is None:
            raise ValueError("Invalid ParentNode: requires children")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
