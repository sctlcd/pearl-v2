# [Pearl](https://sctlcd-pearl-latest-version.herokuapp.com/)

<img src="https://github.com/sctlcd/pearl-latest-version/blob/master/design/mockups.png" alt="Pearl" width="700">

<dd>Do you like creative activities, Arts and Crafts and making things by yourself with your hands and your creativity ?</dd>
<dt>This website is a pearl to you!</date_to_long_string>
<dt>At Pearl's you can purchase arts and crafts supplies and sharing customers' work of art in the meantime as getting inspiration from other customers' creative work in the gallery</dt>

[Let me show you!](https://sctlcd-pearl-latest-version.herokuapp.com/)

**Warning** Because of an issue relative to submitting a form with an uploaded image in my deployed environment I did set up the image field in the gallery model as not required for limiting the impact of the issue which has been solved just before my project deadline submission. I set up initially the gallery image field as required. I will set it back to required in the future.

---

# Table of Contents <a name="TableOfContents"></a>

1. [About](#About)
	- [Why this project?](#WhyThisProject)

1. [UX](#UX)

	- [User Stories](#UserStories)
	- [Design](#Design)
		- [Framework](#Framework)
		- [Color Scheme](#ColorScheme)
		- [Icons](#Icons)
		- [Typography](#Typography)

2. [Features](#Features)

	- [Existing Features](#ExistingFeatures)

3. [Technologies Used](#TechnologiesUsed)

	- [Front-End Technologies](#Front-end-technologies)
  - [Back-End Technologies](#Back-end-technologies)

4. [Relational scheme](#RelationalScheme)

5. [Testing](#Testing)

	- [User story validation](#UserStoryValidation)
	- [Layout responsiveness](#LayoutResponsiveness)
	- [Compatibility](#Compatibility)
	- [Testing left](#Testingleft)
	- [Validators](#Validators)
	- [Known Issues](#KnownIssues)

6. [Deployment](#Deployment)

	- [Deployment – Live website](#Deploymentlivewebsite)
	- [Deployment – Run locally](#Deploymentrunlocally)

7. [Credits](#Credits)

	- [Content](#Content)
	- [Media](#Media)
	- [Code](#Code)
	- [Acknowledgements](#Acknowledgements)

---

## About <a name="About"></a>

The primary purpose of Pearl is to purchase arts and crafts supplies. Its secondary purpose is to share customers' work of art in the meantime as getting inspiration from other customers' creative work in the gallery. And this anytime, anywhere as this application is available on various devices as desktops, tablets and mobile.

Back to [top](#TableOfContents)

---

### Why this project? <a name="WhyThisProject"></a>

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, the **Full Stack Frameworks With Django** module. The objective of this milestone project is building a full-stack site based around business logic used to control a centrally-owned dataset, setting up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

My modern responsive e-commerce arts and craft supplies shop built using HTML, CSS, Material Design for Bootstrap, JavaScript, jQuery, Django, Python, PostgreSQL.

Back to [top](#TableOfContents)

---

## UX  <a name="UX"></a>

### User Stories <a name="UserStories"></a>

"***As a user, I want to _____***"

[v] successfully implemented
[x] not yet implemented

- :heavy_check_mark: view the site from any device (mobile, tablet, desktop).
- :heavy_check_mark: be able to log in.
- :heavy_check_mark: be able to log out.
- :heavy_check_mark: be able to register.
- :heavy_check_mark: filter and search amongst all products.
- :heavy_check_mark: view all products.
- :heavy_check_mark: view a product details.
- :heavy_check_mark: add products with an image as an admin.
- :heavy_check_mark: add products without an image as an admin.
- :heavy_check_mark: edit products with an image as an admin.
- :heavy_check_mark: edit products without an image as an admin.
- :heavy_check_mark: delete products as an admin.
- :heavy_check_mark: view gallery images.
- :heavy_check_mark: view a gallery image.
- :heavy_check_mark: share a gallery image as a logged in user.
- :heavy_check_mark: add a gallery item with an image as an admin.
- :heavy_check_mark: add a gallery item without an image as an admin.
- :heavy_check_mark: edit a gallery item with an image as an admin.
- :heavy_check_mark: edit a gallery item without an image as an admin.
- :heavy_check_mark: delete a gallery image as an admin.
- :heavy_check_mark: approved a gallery image as an admin.
- :heavy_check_mark: view my profile as a logged in user.
- :heavy_check_mark: update my profile as a logged in user.
- :heavy_check_mark: update my profile as logged in user.
- :heavy_check_mark: add products to my bag.
- :heavy_check_mark: checkout my order.
- :heavy_check_mark: send a contact request.


Back to [top](#TableOfContents)

---

### Design <a name="Design"></a>

I did choose a warm and joyful dominant orange [#fc9601](https://placehold.it/15/fc9601/fc9601) combinated with sober colors ranging between off-white [#fafafa](https://placehold.it/15/fafafa/fafafa) and black with a range of grey.
I choose the [logo](https://github.com/sctlcd/pearl-latest-version/blob/master/media/logo/pearl-min.png) and all the website [images](https://github.com/sctlcd/pearl-latest-version/tree/master/media) relative to arts and crafts and creative activities. I selected the main home page image, [hero-image-background](https://github.com/sctlcd/pearl-latest-version/blob/master/media/home/hero_image/hero-image-background-min.jpg), as I found it absolutely beautiful, very eye-catchy and intriguing. It catches the customers/visitors' attention and makes them very curious about it.
I decided to implement a customers' gallery and offer the possibility to share your own piece of art and getting inspiration from other customers' art work. I believe this feature is an very interesting one as it involves the customers in the website building. They are in a way actor of the gallery page building and content.  

Back to [top](#TableOfContents)

---

#### Framework <a name="Framework"></a>

- [Material Design for Bootstrap 4.19.1](https://mdbootstrap.com/)
	- I really like the modern and clean layout of Material Design and the ease of use and standards of Bootstrap so I wanted to give a try and getting familiar with Material Design for Bootstrap
- [jQuery 3.5.1](https://jquery.com/)
	- For the purpose of keeping the JavaScript minimal
- [Django 3.1.1](https://www.djangoproject.com/)


Back to [top](#TableOfContents)

---

#### Color Scheme <a name="ColorScheme"></a>

- [#fc9601](https://placehold.it/15/fc9601/fc9601)
- [#6a6a6e](https://placehold.it/15/6a6a6e/6a6a6e)
- [#fafafa](https://placehold.it/15/fafafa/fafafa)
- [#efefef](https://placehold.it/15/efefef/efefef)
- [#6c757d](https://placehold.it/15/6c757d/6c757d)
- [#d8d8d8](https://placehold.it/15/d8d8d8/d8d8d8)
- [#d6d4d4](https://placehold.it/15/d6d4d4/d6d4d4)
- [#dee2e6](https://placehold.it/15/dee2e6/dee2e6)
- [#000](https://placehold.it/15/000/000)

Back to [top](#TableOfContents)

---

#### Icons <a name="Icons"></a>

- [Font Awesome 5.14.0](https://fontawesome.com/)
 - It fits my needs for this project

Back to [top](#TableOfContents)

---

#### Typography <a name="Typography"></a>

- [Google Fonts](https://fonts.google.com/) were used across the site:
	- [Open Sans](https://fonts.google.com/specimen/Open+Sans) - default font
	- [Smythe](https://fonts.google.com/specimen/Smythe) - showcase section on home page
	- [Crafty Girls](https://fonts.google.com/specimen/Crafty+Girls) - customer review section on home page

Back to [top](#TableOfContents)

---

## Features <a name="Features"></a>

### Existing Features <a name="ExistingFeatures"></a>

#####  Navigation bar

- A top navbar with the logo and the name of the website, menu items and dropdown menu items : Gallery, My Account, Basket and a product search bar.
- a navbar with the products menu items and dropdown menu items

##### Footer

- Social medias to get connected
- 3 sections : Company presentation, links to other pages of the website (not implemented), contact section with a contact button redirecting to the contact page.
- coypright mention with my name and my gitbhub repository

Back to [top](#TableOfContents)

---

##### Home page

- 6 sections: Shop now, website order feature offered, target activities, customer reviews, Share your work of art, Stay tune (newsletter subscription not implemented, for presentation purpose)

##### Products page

- A Product collection presented in a "mozaic format"

##### Products details page

- A page with product details: name, description, proce, rating, product image

Back to [top](#TableOfContents)

---

##### Products management page

- Add Product page with add product form
- Edit Product page with edit product form

##### Gallery page

- A gallery of customers' work of art

##### Share gallery page

- A share gallery item form can be submitted

##### Gallery management page

- Add Gallery item page with add gallery item form
- EditGallery item page with edit gallery item form

Back to [top](#TableOfContents)

---

##### Profile page

- To view and update your profile


##### Shopping bag page

- To view and adjust your shopping bag

##### Checkout page

- To checkout orders

Back to [top](#TableOfContents)

---

##### No result found page

- Humoristic picture and message letting know the user no result have been found matching with his/her search.
- Link redirecting to Products Home.

Back to [top](#TableOfContents)

---

##### Error pages

- I created the 404 page - No page found and 500 page - Internal server error

Back to [top](#TableOfContents)

---

## Technologies Used <a name="TechnologiesUsed"></a>

- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Atom](https://atom.io/) - Used as a local IDE.
- [Compressjpeg](https://compressjpeg.com/) - Used to compress images for loading faster
- [Techsini](https://techsini.com/multi-mockup/) - Used to generate multi-device website mockup
- [Ngrok 2.3.35](https://ngrok.com/) - Expose a local web server to the public internet over secure tunnels

Back to [top](#TableOfContents)

---

### Front-End Technologies <a name="Front-end-technologies"></a>

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Material Design for Bootstrap 4.19.1](https://mdbootstrap.com/) - used as a front-end framework for building responsive, mobile-first websites and apps
- [JavaScript](https://www.javascript.com/) - Used for user interactions.
- [jQuery 3.5.1](https://jquery.com/) - JavaScript library, used to simplify some of the DOM manipulations.
- [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make secured payments
- [Amazon AWS S3](https://aws.amazon.com/) - Used to store staticfiles and media folders and files.

Back to [top](#TableOfContents)

---

### Back-End Technologies <a name="Back-end-technologies"></a>

- [Python 3.8](https://www.python.org/) - Used as the back-end programming language.
- [Django 3.1.1](https://www.djangoproject.com/) - Used as Python web framework.
- [Heroku](https://www.heroku.com/) - Used for app hosting.
- [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.

Back to [top](#TableOfContents)

---

## Relational scheme <a name="RelationalScheme"></a>

The Relational scheme diagram can be found [here](https://github.com/sctlcd/pearl-latest-version/blob/master/design/relational-scheme.png)


## Testing <a name="Testing"></a>

### User story validation <a name="UserStoryValidation"></a>

:heavy_check_mark: *as expected*
:x: *not as expected*

- :heavy_check_mark: view the site from any device (mobile, tablet, desktop).
- :heavy_check_mark: be able to log in.
- :heavy_check_mark: be able to log out.
- :heavy_check_mark: be able to register. (see known issue section)
- :heavy_check_mark: filter and search amongst all products.
- :heavy_check_mark: view all products.
- :heavy_check_mark: view a product details.
- :heavy_check_mark: add products with an image as an admin.
- :heavy_check_mark: add products without an image as an admin.
- :heavy_check_mark: edit products with an image as an admin.
- :heavy_check_mark: edit products without an image as an admin.
- :heavy_check_mark: delete products as an admin.
- :heavy_check_mark: view gallery images.
- :heavy_check_mark: view a gallery image.
- :heavy_check_mark: share a gallery image as a logged in user.
- :heavy_check_mark: add a gallery item with an image as an admin.
- :heavy_check_mark: add a gallery item without an image as an admin.
- :heavy_check_mark: edit a gallery item with an image as an admin.
- :heavy_check_mark: edit a gallery item without an image as an admin.
- :heavy_check_mark: delete a gallery image as an admin.
- :heavy_check_mark: approved a gallery image as an admin.
- :heavy_check_mark: view my profile as a logged in user.
- :heavy_check_mark: update my profile as a logged in user.
- :heavy_check_mark: update my profile as logged in user.
- :heavy_check_mark: add products to my bag.
- :heavy_check_mark: checkout my order.
- :heavy_check_mark: send a contact request.

---

### Layout responsiveness <a name="LayoutResponsiveness"></a>

|  | Moto G4 | Galaxy S5 | Pixel 2 | Pixel 2 XL | iPhone 5/SE | iPhone 6/7/8 | iPhone 6/7/8 Plus | iPhone X | Surface Duo | iPad | iPad Pro | Desktop 1024px | Desktop > 1200px |
| :--- | :--- | :---| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| website is responsive <= 767 px | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | n/a | n/a | n/a | n/a |
| website is responsive >= 768 px | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Good | Good | Good | Good |
|**bag app** |
| Navigation bar: logo / links / search | Good |  | Good  |  |  | Good |  | Good |  | Good |  | Good |  |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good |  | Good |  | Good |  | Good |  | Good |  | Good |
|**checkout app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text | Good |  |  Good |  | Good |  | Good |  | Good |  | Good |  | Good |
| Footer: text / links | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
|**Contact app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Gallery app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Home app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Product app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Profile app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |


Back to [top](#TableOfContents)

---

### Compatibility <a name="Compatibility"></a>

I tested the website across the 6 main browsers in both desktop and mobile configuration to ensure a large number of users can use it successfully.

- Chrome v.87.0
- Edge v.87.0
- Firefox v.84.0
- Safari v.5.1.7 for Windows 10
- Opera v.73.0
- Internet Explorer v.11

|All pages | Chrome | Edge | Firefox | Safari | Opera | IE |
| :--- | :--- | :---| :--- | :--- | :--- | :--- |
| Expected appearance | Good | Fair | Good | Poor | Good | Poor |
| Expected responsiveness | Good | Good | Good | Poor | Good | Poor |

- IE: Some CSS3 properties and HTML5 elements are not fully supported

- Safari v.5.1.7: It’s an outdated version and lacks many of the features present in the latest version of Safari. The last version of Safari for Windows was released on May 9, 2012.

Back to [top](#TableOfContents)

---

### Testing left <a name="Testingleft"></a>

- There is no way to install the latest version of the Safari browser on Windows 10 as Apple stopped developing Safari for Windows operating system long ago.
For testing this website on the latest version of Safari, I will have to install the newest version of macOS on Windows 10 in a virtual machine.

Back to [top](#TableOfContents)

---

### Validators <a name="Validators"></a>

**HTML**
- [W3C HTML Validator](https://validator.w3.org/)
	- Django template syntax not understood
	- No error

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
	- No error

**Javascript**
- [Javascript Validator](https://jshint.com/)
	- No error

**Chrome DevTools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
	- Console Navigating through the Website rendered no critical fails/errors in the console that were necessary to fix.

**Python**
- [Python validator](http://pep8online.com/)
 - No error

Back to [top](#TableOfContents)

---

### Known Issues <a name="KnownIssues"></a>

- top/down page visible when scroll down then scroll up to window scroll = 0 when mobile menu is collapse
- Sign up issue relative to sending email. Implementing email backend to fix this issue
- Set image gallery back to required.
- Create products and gallery sub-directories in media folder containing respectively product images and gallery images.

Back to [top](#TableOfContents)

---

## Deployment <a name="Deployment"></a>

### Deployment – Live Website <a name="Deploymentlivewebsite"></a>

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. Once you have the project setup locally, you can proceed to deploy it remotely with the following steps:

- Create a **requirements.txt** file so Heroku can install the required dependencies to run the app:
    - `sudo pip3 freeze --local > requirements.txt`
    - The *requirements.txt* file for this project can be found here: [requirements.txt](https://github.com/sctlcd/pearl-latest-version/blob/master/requirements.txt)
- Create a **Procfile** to tell Heroku what type of application is being deployed using *pearl-latest-version*, and how to run it:
    - `echo web: gunicorn main.wsgi:application > Procfile`
    - The *Procfile* for this project can be found here: [Procfile](https://github.com/sctlcd/pearl-latest-version/blob/master/Procfile)
- Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
- In the Heroku **Resources** tab, navigate to the *Add-Ons* section and search for **Heroku Postgres**. Make sure to select the free *Hobby* level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your *.env* file with your new *database-url* details.
- In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables. You will need to copy/paste all of the *.env* key value pairs into the config variables, but please omit the *development=1* variable; this is only for local deployment.
- Your app should be successfully deployed to Heroku at this point, but you're not quite finished yet!
- Update the *settings.py* file to connect the remote database using this Python package: `dj_database_url`
- Re-build the migrations and create a superuser to your new remote database using the instructions in the *local deployment* section above.
- Sign up for a free [Amazon AWS](https://aws.amazon.com/) account in order to host your *staticfiles* and *media* files. From the **S3 buckets** section, you'll need to create a new unique bucket. Follow these next steps to complete the setup:

**Permissions** > **CORS configuration**:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

**Permissions** > **Bucket Policy**:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<x>/*"
        }
    ]
}
```

*! IMPORTANT ! - on the **Resource** line above, be sure to replace `<x>` with your **AWS bucket arn** details, but retain the `/*` at the end.* It should look similar to this:
    - `"Resource": "arn:aws:s3:::my-bucket-name/*"`

- From here, you'll need to navigate to the **IAM** section of AWS.
    - Create a *New Group* and be sure to select your existing S3 Bucket details to attach.
    - Create a *New Policy* and a *New User* in the IAM section as well, then attach these to the Group you just built.
- In your CLI-terminal, you should now be able to push the static files to AWS if everything is configured properly using this command:
    - `python manage.py collectstatic`
- Sign up for a free [Stripe](https://stripe.com) account. Navigate to the **Developers** section, and click on **API Keys**. You should have two confidential keys which need to be added to your *.env* file, as well as your Heroku config vars. These keys are:
    - `Publishable Key`: **pk_test_key**
    - `Secret Key`: **sk_test_key**

Congratulations! Your project should be completely setup and ready for remote deployment!

### Deployment – Run Locally <a name="Deploymentrunlocally"></a>

It's highly recommended to work in a virtual environment, but not absolutely required.

In order to run this project locally on your own system, you will need the following installed (as a bare minimum):

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green "*Clone or download*" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
    - `git clone https://github.com/sctlcd/pearl-latest-version.git`
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file with your own credentials. An example *.env* file can be found here ([.env_sample](project/.env_sample)).
    - *Note: the example .env file contains environmental variables for both local and remote deployment. (see below for remote deployment details)*
- Install all requirements from the [requirements.txt](project/requirements.txt) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- In the IDE terminal, use the following command to launch the Django project:
    - `python manage.py runserver`
- The Django server should be running locally now on **http://127.0.0.1:8000** (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.
- When you run the Django server for the first time, it should create a new *SQLite3* database file: **db.sqlite3**
- Next, you'll need to make migrations to create the database schema:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- In order to access the Django *Admin Panel*, you must generate a superuser:
    - `python manage.py createsuperuser`
    - (assign an admin username, email, and secure password)

Once the database migrations and superuser have been successfully completed, Django should migrate the existing *migrations.py* files from each app to configure the following relational schema:

[Relational Schema](https://github.com/sctlcd/pearl-latest-version/blob/master/design/relational-scheme.png)

Back to [top](#TableOfContents)

---

## Credits <a name="Credits"></a>

- My inspiration comes from:
- [Etsy](https://www.etsy.com/) - E-commerce website focused on handmade or vintage items and craft supplies
- [Cultura](https://www.cultura.com/)- E-commerce website specialized in cultural, arts and crafts goods and leisure activities

Back to [top](#TableOfContents)

---

### Content <a name="Content"></a>

- Baker Ross [bakerross](https://www.bakerross.ie/)

Back to [top](#TableOfContents)

---

### Media <a name="Media"></a>

Sources of the images used on this site:

- From media/home/hero_image sub-directory
	- [](https://pixabay.com/fr/photos/outil-outils-%C3%A9quipement-travail-1957451/) - [Pixabay](https://pixabay.com/) | copyright [coyot](https://pixabay.com/fr/users/coyot-2009089/)
	- [](https://pixabay.com/fr/photos/laine-d-acier-sombre-firespin-458840/) - [Pixabay](https://pixabay.com/) | copyright [463259](https://pixabay.com/fr/users/463259-463259/)  

- From media/home/image_showcases sub-directory
	- [](https://www.flickr.com/photos/woolgenie/11130456836/in/photolist-hXyv3d-5Y9E3c-5nT1q6-9fntLS-hw5rUx-bqVeMj-fdLe7t-BEdCfZ-soJx4-bNxP4i-63nP6c-e5cPNV-ckHujG-a2CVXo-8cvxSy-db7Yc5-81Y6dy-cfSt2L-dy4o3n-6fhExi-6p7Cpn-o9UymA-4wiG4Q-gwcN4-7t4EFt-7tp6xA-6UzTPj-7C4uvk-9Zzhxg-8pfMEs-aAhfP5-CZhs-7teK8f-biUirX-7jSHo1-4m89zu-7viAh3-6bwUfh-oxL6Z-7viAZS-iSoZF-5dtWk7-dLLYgg-4e37c3-8fi2Lx-85fwdc-rWakmW-dC8TzU-dgMAa9-2ehg9Ey) - [Flickr](https://www.flickr.com) | copyright [Heather](https://www.flickr.com/photos/woolgenie/)
	- [](https://www.pexels.com/photo/assorted-color-great-board-decor-lot-1539581/) - [Pexels](https://www.pexels.com/) | copyright [Tim Mossholder](https://www.pexels.com/@timmossholder)
	- [](https://www.flickr.com/photos/wespeck/4473683746/) - [Flickr](https://www.flickr.com) | copyright [gfpeck](https://www.flickr.com/photos/wespeck/)
	- [](https://www.flickr.com/photos/mikecogh/43105291024/) - [Flickr](https://www.flickr.com) | copyright [Michael Coghlan](https://www.flickr.com/photos/mikecogh/)

- From media/home/testimonials sub-directory
	- https://pixabay.com/fr/photos/mod%C3%A8le-femme-portrait-336658/  Image par Free-Photos de Pixabay
	- https://pixabay.com/fr/photos/jeune-fille-%C3%A9changisme-coiffure-1245835/ Image par Free-Photos de Pixabay
	- https://www.pexels.com/photo/portrait-photo-of-man-in-white-crew-neck-t-shirt-with-assorted-hand-tools-in-background-1139743/ de Juan Pablo Serrano Arenas https://www.pexels.com/@juanpphotoandvideo

- From media/home/gallery sub-directory
	- [gallery-background-1920-min.jpg](https://www.pexels.com/photo/apple-device-camera-camera-lens-desk-593325/) - [Pexel](https://www.pexels.com/) | copyright [Jessica Lewis](https://www.pexels.com/@thepaintedsquare)

- From media/logo sub-directory
	- [pearl-min.png](https://www.flaticon.com/free-icon/knowledge_3603994) - [Flaticon](https://www.flaticon.com/) | copyright [Freepik](https://www.flaticon.com/authors/freepik)

- From media/error sub-directory
	- [no-results-found-min.jpg](https://all-free-download.com/free-vector/download/exploration-job-background-searching-man-sketch-cartoon-design_6844384.html) - [Free vectors](https://all-free-download.com/free-vector/) | copyright [BSGStudio](http://buysellgraphic.com/)

- From media directory
	- [bakerross](https://www.bakerross.ie/)
	- [pixabay](https://pixabay.com/)
	- [pexels](https://www.pexels.com/)
	- [unsplash](https://unsplash.com/)
	- [flickr](https://www.flickr.com/)

Back to [top](#TableOfContents)

---

### Code <a name="Code"></a>

- Environment variables - [Igor Basuga](https://github.com/bravoalpha79) Tutor at [Code Institute](http://codeinstitute.net)
- Environment variables - Code Institute archive resources
- Ngrok - [ngrok](https://ngrok.com/)
- Using ngrok on Windows-10 - [youtube](https://www.youtube.com/watch?v=9gaaVbX0USI&ab_channel=ChuckSeverance)
- Testing our Django App to be publicly accessible using NGROK - [medium](https://medium.com/@iot24hours/testing-our-django-app-to-be-publicly-accessible-using-ngrok-9b73851c46e0)
- jQuery documentation - [jQuery](https://jquery.com/)
- Favicon in django app - [stackoverflow](https://stackoverflow.com/questions/21938028/how-can-i-get-a-favicon-to-show-up-in-my-django-app)
- Material Design for Bootstrap documentation - [mdbootstrap](https://mdbootstrap.com/)
- How to integrate mdbootstrap with django - [mdbootstrap](https://mdbootstrap.com/articles/jquery/how-to-integrate-mdbootstrap-with-django/)
- mdb input number [mdbootstrap](https://mdbootstrap.com/docs/jquery/forms/inputs/)
- Creating a modal image gallery with bootstrap components - [css-tricks](https://css-tricks.com/creating-a-modal-image-gallery-with-bootstrap-components/)
- How to - Portfolio Gallery with Filtering - [w3schools](https://www.w3schools.com/howto/howto_js_portfolio_filter.asp)
- Portfolio Filter Gallery HTML CSS & JavaScript | Image Category Filtering [webdevtrick](https://webdevtrick.com/portfolio-filter-gallery/)
- How to - Lightbox - [w3schools](https://www.w3schools.com/howto/howto_js_lightbox.asp)
- Material Design Full Screen Modal - [mdbootstrap](https://mdbootstrap.com/snippets/jquery/mustafaozkaya/789907#html-tab-view)
- How to change your commit messages in Git? - [github](https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4)
- How to limit the maximum value of a numeric field in a Django model? [stackoverflow] - (https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
- Python perform append at beginning of list - [geeksforgeeks] - https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/
- How to upload files with django - [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)
- How to crop an image in css - [educative](https://www.educative.io/edpresso/how-to-crop-an-image-in-css)
- Set favicon in django admin - [stackoverflow](https://stackoverflow.com/questions/34959897/set-favicon-in-django-admin)
- Change the display format of time fields - [stackoverflow](https://stackoverflow.com/questions/7216764/in-the-django-admin-site-how-do-i-change-the-display-format-of-time-fields)
- Automatic datetime fields - [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tips/2016/05/23/django-tip-4-automatic-datetime-fields.html)
- Delete a git commit but keep the changes [stackoverflow](https://stackoverflow.com/questions/15772134/can-i-delete-a-git-commit-but-keep-the-changes)
 - You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path - [stackoverflow](https://stackoverflow.com/questions/48455469/youre-using-the-staticfiles-app-without-having-set-the-static-root-setting-to-a)
 - Python django error oserror winerror 123 the filename directory name or vol - [stackoverflow](https://stackoverflow.com/questions/56166319/python-django-error-oserror-winerror-123-the-filename-directory-name-or-vol)
 - Modify Title and Header Django Admin Interface - [medium](https://adiramadhan17.medium.com/modify-title-and-header-django-admin-interface-a6ad6e470d92)
 - Customizing HTTP error web pages 404, 500, 403 and 400 in Django - [lavatechtechnology](http://lavatechtechnology.com/post/customizing-http-error-web-pages-404-500-403-and-400-in-django/)
 - Equivalent of export command in Windows - [superuser](https://superuser.com/questions/1500272/equivalent-of-export-command-in-windows)
 - Heroku Django Deploy Stripe Issue - No module named 'stripe'
 - [stackoverflow](https://stackoverflow.com/questions/51509121/heroku-django-deploy-stripe-issue-no-module-named-stripe/51509169)
 - Readme file information - [Tim Nelson](https://github.com/TravelTimN) Software Developer and Tutor at [Code Institute](http://codeinstitute.net)

Back to [top](#TableOfContents)

---

### Acknowledgements <a name="Acknowledgements"></a>

- [Anthony Ngene](https://github.com/tonymontaro)
	- Thanks to my Code Institute mentor for his time, suggestions, constructive feedback and availability.  
- CI Tutor support for their help in order to understand some issues and their friendliness.

Back to [top](#TableOfContents)

---
