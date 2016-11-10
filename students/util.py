from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(objects, size, request, context, var_name='object_list'):
    """Paginate objects provided by view"""

    # apply pagination
    paginator = Paginator(objects, size)
    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    context['var_name'] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context
