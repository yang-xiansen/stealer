# Create your views here.
from stealer import route
from tools.type import Video


def fetch(request):
    return route.fetch(Video.DOUYIN, request)


def download(request):
    return route.download(Video.DOUYIN, request)
