from tethys_sdk.base import TethysAppBase, url_map_maker


class SethDesign(TethysAppBase):
    """
    Tethys app class for Seth Design.
    """

    name = 'Seth Design'
    index = 'seth_design:home'
    icon = 'seth_design/images/icon.gif'
    package = 'seth_design'
    root_url = 'seth-design'
    color = '#f39c12'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='seth-design',
                controller='seth_design.controllers.home'
            ),
        )

        return url_maps
