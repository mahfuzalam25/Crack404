from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Author
from .forms import BlogForm
def bloghome(request):
    allPosts = Post.objects.all().order_by('-publish_date')  # Fetch all posts
    return render(request, 'blog/blog.html', {'allPosts': allPosts})

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'blog/blogpost.html', {'post': post})




def addblog(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        author_id = request.POST.get('author')
        password = request.POST.get('password')

        if author_id:
            # Verify existing author password
            try:
                author = Author.objects.get(id=author_id)
                if not author.verify_password(password):
                    messages.error(request, "Incorrect password! Please try again.")
                    return render(request, 'blog/BlogForm.html', {'form': form, 'authors': authors})
            except Author.DoesNotExist:
                messages.error(request, "Author not found!")
                return render(request, 'blog/BlogForm.html', {'form': form, 'authors': authors})
        else:
            # Create a new author if no existing author is selected
            name = request.POST.get('name')
            designation = request.POST.get('designation')
            new_password = request.POST.get('new_password')
            author_image = request.FILES.get('author_image', None)

            if not name or not designation or not new_password:
                messages.error(request, "Please provide all details for a new author.")
                return render(request, 'blog/BlogForm.html', {'form': form, 'authors': authors})

            author, created = Author.objects.get_or_create(name=name)
            if created:
                author.designation = designation
                author.set_password(new_password)
                author.image = author_image
                author.save()
            else:
                messages.error(request, "Author name already exists. Choose a different name.")
                return render(request, 'blog/BlogForm.html', {'form': form, 'authors': authors})

        if form.is_valid():
            post = form.save(commit=False)
            post.author = author
            post.save()
            messages.success(request, "Your blog has been posted successfully!")
            return redirect('/')
        else:
            messages.error(request, "There was an error in your form. Please check again.")

    else:
        form = BlogForm()

    return render(request, 'blog/BlogForm.html', {'form': form, 'authors': authors})
