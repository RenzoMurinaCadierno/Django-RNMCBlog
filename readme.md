RNMC Social
========================================

Overview
----------------------------------------

The idea behind this project is to let users comment on blog posts only I create, what would basically be the foundation of one-way blogging pages like Wordpress.

As an admin, the site gives me the chance to create blog posts delete and edit them, as well as revising user comments before they are published to emulate a 'moderator' role. This site's whole functionality is handled by Class-based views using Django framework. Since my aim here is to work at wiring the back-end, the front-end is a bit too basic. It was made with Bootstrap 3 and some custom CSS.

A working instance of this app is deployed at [this Heroku site](https://rnmcblog.herokuapp.com/).

As for my other projects, please feel free to go to [my GitHub page](https://github.com/RenzoMurinaCadierno) to check them out. I am still on my learning tracks, so you will see new projects frequently. I specialize in Python and Javascript, and whatever I upload is normally related to web, game and app developing, or Python scripting for multiple purposes.

I have put together this example up following Jose Portilla's proposed exercise on his ['Python and Django Full Stack Web Developer Bootcamp'](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/) Udemy course. Definitely check it out if you want to learn this framework, HTML, CSS, JQuery, Bootstrap and Python basics from scratch.

The gradient rotation effect in some texts and buttons was taken from [Shivam Thapliyal's project](https://codepen.io/thapliyalshivam/details/dvgXVO). Moreover, the custom edition option available when you highlight text inside a TextArea was copied from the [Medium Style Editor project](https://github.com/yabwe/medium-editor) made by user "yabwe" in GitHub. Both are impressive additions to any media page, I recommend them at any time.

Instructions
------------------------------------------

Nothing new other than what you basically do in a blog app, pretty much intuitive.

As a **user** you can:

- Navigate to each Post by clicking on their names on the main page. You will be redirected to the post page, where you can check the content and comments out.
- On a post page there is a button to add a comment which will allow you to type a comment in a fully customizable text-box. Note that your comment will NOT be published instantly, since the Admin has to approve it first.

As an **admin** you can:

- Create a post using the "New Post" option in the navbar.
- Once the post is created, it will fall in the "Drafts" storage page before being published. You can edit or delete it if you desire, or publish it for it to appear visible to all visitors.
- Edit or delete posts that are already published, by visiting the post's page and using the provided icons.
- Accept or delete users' posts before they are visible to everyone, on the same fashion explained on the last bullet.

### Thank you for reading and for taking your time to check this project out!
