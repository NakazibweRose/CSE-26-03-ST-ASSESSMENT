from django.shortcuts import render, redirect
from .models import VideoList

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def video_listing(request):
    videos = VideoList.objects.order_by('-publishing_date')

    return render(request, 'video_listing.html', {'videos': videos})

def upload_video(request):

    if request.method == 'POST':

        errors = {}

        title = request.POST.get('title')
        description = request.POST.get('description')
        quality = request.POST.get('quality')
        publishing_date = request.POST.get('publishing_date')

        video_file = request.FILES.get('video_file')
        thumbnail = request.FILES.get('thumbnail')

        if not title:
            errors['title'] = 'Title is required.'

        if not quality:
            errors['quality'] = 'Video quality is required.'

        if not publishing_date:
            errors['publishing_date'] = 'Publishing date is required.'

        if not video_file:
            errors['video_file'] = 'Video file is required.'

        if not thumbnail:
            errors['thumbnail'] = 'Thumbnail is required.'

        if errors:
            return render(
                request,
                'upload.html',
                {
                    'errors': errors
                }
            )

        video = VideoList.objects.create(
            title=title,
            description=description,
            quality=quality,
            publishing_date=publishing_date,
            video_file=video_file,
            thumbnail=thumbnail
        )

        return render(
            request,
            'upload.html',
            {
                'success': 'Video uploaded successfully!'
            }
        )

    return render(request, 'upload.html')