import logging

LOG = logging.getLogger(__name__)


class Resource(object):
    """
    A demo class
    """

    def get(self, author=None):
        """
        A method to demo that partial coverage is not displayed

        :type author: str
        :param author: The author

        :rtype: bool
        :return: Partial coverage is not shown.
        """
        if author:
            LOG.info('Author: {author}'.format(author=author))

        return False
