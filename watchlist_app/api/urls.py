from django.urls import path, include 
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchDetailAV,WatchListAV,ReviewList,ReviewDetail,ReviewCreate, StreamPlatformVS
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamPlatform')



urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('',include(router.urls)),
    # path('stream/',StreamPlatformAV.as_view(),name='stream-platform-av'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-platform-detail'),
    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-Detail')
]
