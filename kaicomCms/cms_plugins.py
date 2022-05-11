from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PollPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel  # model where plugin data are saved
    name = _("Poll Plugin")  # name of the plugin in the interface
    render_template = "plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context