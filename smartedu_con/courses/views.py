from django.shortcuts import render
from .models import Course, Category, Tag


# def course_list(request):
#     courses = Course.objects.all().order_by('-date')
#     categories = Category.objects.all()
#
#     context = {
#         'courses': courses,
#         'categories': categories
#     }
#
#     return render(request, 'courses.html', context)

def course_list(request, category_slug=None, tag_slug=None):
    courses = Course.objects.filter(available=True).order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if category_slug:
        courses = courses.filter(category__slug=category_slug)

    if tag_slug:
        courses = courses.filter(tags__slug=tag_slug)

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses.html', context)


def category_list(request, category_slug):
    courses = Course.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses.html', context)


def tag_list(request, tag_slug):
    courses = Course.objects.filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses.html', context)


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)

    context = {
        'course': course
    }

    return render(request, 'course.html', context)
