<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.flaticon.com/de/kostenloses-icon/roboter_3558860">
    <img src="website/static/images/icon.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Deep Feature Matching</h3>

  <p align="center">
    A social media bot, capable of posting to Instagram and Whatsapp!
    <br />
    <a href="#readme-toc"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#pictures-and-videos">View Demo</a>
    ·
    <!-- <a href="https://github.com/mirkosprojects/socialmedia-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/mirkosprojects/socialmedia-bot/issues">Request Feature</a>
    · -->
    <a href="https://www.flaticon.com/de/kostenloses-icon/roboter_3558860"> Icon </a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<a name="readme-toc"></a>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#creating-a-facebook-business-account">Creating a Facebook Business Account</a></li>
        <li><a href="#creating-an-instagram-business-account">Creating an Instagram Business Account</a></li>
        <li><a href="#linking-to-facebook">Linking to Facebook</a></li>
        <li><a href="#getting-an-access-token">Getting an Access Token</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#starting-the-app">Starting the app</a></li>
        <li><a href="#sign-up">Sign up</a></li>
        <li><a href="#updating-credentials">Updating credentials</a></li>
        <li><a href="#creating-a-contact-list">Creating a contact list</a></li>
        <li><a href="#creating-your-first-post">Creating your first post</a></li>
      </ul>
    <li><a href="#next-steps">Next steps</a></li>
    <ul>
        <li><a href="#running-the-app-on-the-local-network">Running the app on the local network</a></li>
        <li><a href="#publishing-the-app-to-the-internet">Publishing the app to the internet</a></li>
      </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#pictures-and-videos">Pictures and Videos</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

The HKA Social Media Bot is a tool capable of posting images and messages to various social media websites. ~~Keep your workflow steady with scheduled posts and automatic image generation!~~

<!-- The HKA Social Media Bot is a command line tool, capable of sending or posting various messages to social media websites. Keep your workflow steady with scheduled posts and automatic image generation! -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ### Built With
* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- GETTING STARTED -->
## Getting Started

### Installation
* Creating a new virtual environment

  This app is built on [Flask][flask], which recommends creating a new conda environment
  ```sh
  conda create -n socialmediabotEnv python=3.9.7 anaconda
  conda activate socialmediabotEnv
  ```

  > **Note**
  > If you have closed your terminal window, you can reactivate your virtual environment by typing ```conda activate socialmediabotEnv``` again

* Clone the repo
   ```sh
   git clone https://github.com/mirkosprojects/socialmedia-bot.git
   ```
* Install dependencies
  ```sh
  cd socialmedia-bot
  pip install -r requirements.txt
  ````
  For more information about the dependencies see [requirements][requirements]

### Creating a Facebook Business Account

```
HOW TO CREATE OR CONVERT TO A FACEBOOK BUSINESS ACCOUNT
```

### Creating an Instagram Business Account

```
HOW TO CREATE OR CONVERT TO AN INSTAGRAM BUSINESS ACCOUNT
```

### Linking to Facebook
```
HOW TO LINK WHATSAPP AND INSTAGRAM ACCOUNTS TO FACEBOOK
```

### Getting an Access Token

<!-- This program needs your authorization in order to publish to Instagram and Whatsapp. To grant access, login to your Facebook Account and search for HKA SocialMediaBot. 
Click add and grant access to the requested rights.

Once you've granted the required permissions, you will receive an Access Token. Copy this Token and continue with <a href="#usage">Usage</a> -->

```
HOW TO ADD FACEBOOK APP TO ACCOUNT AND RECEIVE ACCESS TOKEN
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Starting the app
* Starting the app
   ```sh
   python main.py
   ```
   Once the app has started, it will output an ip adress (usually 127.0.0.1:5000), copy and paste it in your browser

### Sign up
You will be redirected to a Login Page, create a new user account and log in with your email and password.

> **Note**
> The website is running locally on your machine. Email adresses and passwords are stored in a local database at ```socialmedia-bot/instance/database.db```

### Updating credentials
You will have to update your credentials. 
Go to ```Settings``` &rarr; ```Whatsapp```, enter your access token and phone number and click ```Update```.
Repeat this step with your other social media accounts.

### Creating a contact list
Sending messages to whatsapp contacts requires their phone number.
Go to ```Settings``` &rarr; ```Contacts``` and enter the contacts, you wish to message through whatsapp.

### Creating your first post
Go back to ```Home``` and type in a text, you wish to post.
Add an image to the post by clicking on ```Select File``` or drag and drop it.
Select the websites, you wish to post to and click on ```Post```.

> **Note** 
> You can have up to 1000 free whatsapp conversations per month, for more information about pricing, see [pricing][whatsapp-pricing]

> **Note**
> You can post up to 25 pictures on instagram per day

> **Warning**
> In order to post an image through the Graph-API, this program publishes the image on [imgbox.com][imgbox]. This means, your photos will be available on the internet, even after you delete them from Instagram.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PROFESSIONAL USAGE / NEXT STEPS -->
## Next steps

### Running the app on the local network
You can run this application locally on your network, start it as follows
```sh
python main.py --host=0.0.0.0
```
Any other device on the network can now open the website by typing the returned ip adress.

> **Note**
> The default port is 5000. In some cases this port might be used by different applications. You can specify a different port with the ```--port``` argument

> **Warning**
> Multiple users shouldn't access the same account simultaneously

### Publishing the app to the internet
Cloud hosting providers like [DigitalOcean][digital-ocean] can host websites for you, making your app available on the internet.

> **Warning**
> Additional security measures might need to be implemented

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Proof of Concept
    - [x] Whatsapp
    - [x] Instagram
    - [ ] Facebook
    - [ ] Twitter
    - [ ] Snapchat
    - [ ] LinkedIn
- [ ] Webapp
    - [x] Rewrite as webapp using Flask
    - [x] HTML GUI
    - [ ] Database
        - [x] password access
        - [x] storing contacts
        - [ ] storing posts
    - [ ] Publishing to the internet
        - [ ] Security improvements
        - [ ] Deploy using Digital Ocean or other webhost
- [ ] Publishing the facebook app
- [ ] Image Generator using templates
- [ ] Scheduling Posts


<!-- See the [open issues](https://github.com/mirkosprojects/socialmedia-bot/issues) for a full list of proposed features (and known issues). -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PICTURES AND VIDEOS -->
## Pictures and Videos

### Sending a whatsapp message and posting to instagram using Socialbot

![Sending a Whatsapp message][whatsapp-instagram-demo]

### Changing the whatsapp access token and phone number

![Changing Whatsapp settings][whatsapp-settings]

### Editing the contacts

![Editing Contact][contact-settings]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE][license-url] for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
<!-- ## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/mirkosprojects/socialmedia-bot](https://github.com/mirkosprojects/socialmedia-bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Readme Template](https://github.com/othneildrew/Best-README-Template)
* [Flask Template](https://github.com/techwithtim/Flask-Web-App-Tutorial)
* <a href="https://www.flaticon.com/de/kostenlose-icons/bot" title="bot Icons">Bot Icons erstellt von Smashicons - Flaticon</a>
* [iMessage Speech Bubbles](https://codepen.io/AllThingsSmitty/pen/jommGQ)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- SHIELDS -->
[contributors-shield]: https://img.shields.io/github/contributors/mirkosprojects/socialmedia-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/mirkosprojects/socialmedia-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mirkosprojects/socialmedia-bot.svg?style=for-the-badge
[forks-url]: https://github.com/mirkosprojects/socialmedia-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/mirkosprojects/socialmedia-bot.svg?style=for-the-badge
[stars-url]: https://github.com/mirkosprojects/socialmedia-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/mirkosprojects/socialmedia-bot.svg?style=for-the-badge
[issues-url]: https://github.com/mirkosprojects/socialmedia-bot/issues
[license-shield]: https://img.shields.io/github/license/mirkosprojects/socialmedia-bot.svg?style=for-the-badge
[license-url]: https://github.com/mirkosprojects/socialmedia-bot/blob/main/LICENSE

[flask]: https://flask.palletsprojects.com/en/2.2.x/

<!-- RESSOURCES -->
[product-screenshot]: /website/static/images/user_page1.png
[whatsapp-instagram-demo]: website/static/images/whatsapp_instagram_demo.gif
[whatsapp-settings]: website/static/images/settings_whatsapp.png
[contact-settings]: website/static/images/settings_contacts.png
[requirements]: https://github.com/mirkosprojects/socialmedia-bot/blob/main/requirements.txt
[whatsapp-pricing]: https://developers.facebook.com/docs/whatsapp/pricing/
[imgbox]: https://imgbox.com/
[digital-ocean]: https://www.digitalocean.com/

<!-- BUILT WITH -->
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 