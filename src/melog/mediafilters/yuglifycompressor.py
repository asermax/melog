from django.conf import settings
from django.utils.encoding import smart_str
from mediagenerator.generators.bundles.base import Filter


class YuglifyCompressor(Filter):
    def __init__(self, **kwargs):
        super(YuglifyCompressor, self).__init__(**kwargs)
        assert self.filetype in ('css', 'js'), (
            'Yuglify only supports compilation to css and js. '
            'The parent filter expects "%s".' % self.filetype)

    def get_output(self, variation):
        # We import this here, so App Engine Helper users don't get import
        # errors.
        from subprocess import Popen, PIPE
        for inpt in self.get_input(variation):
            try:
                compressor = settings.YUGLIFYCOMPRESSOR_PATH
                command = '{0} --type {1} --terminal'.format(compressor,
                    self.filetype)

                pipe = Popen(command, shell=True, stdin=PIPE, stdout=PIPE,
                    stderr=PIPE, universal_newlines=True)

                output, error = pipe.communicate(smart_str(inpt))

                assert pipe.wait() == 0, \
                    'Command returned bad result:\n%s' % error

                yield output.decode('utf-8')
            except Exception, e:
                raise ValueError("Failed to Yuglify. "
                    "Please make sure that it's in your PATH and that you've "
                    "configured YUGLIFYCOMPRESSOR_PATH in your settings "
                    "correctly.\n"
                    "Error was: %s" % e)
