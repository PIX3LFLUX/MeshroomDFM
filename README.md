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
    Meshroom DFM is a Meshroom implementation of the Deep Feature Matching Algorithm from <a href="https://github.com/ufukefe/DFM">ufukefe</a>.
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
<!-- <a name="readme-toc"></a>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
</details> -->


<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

MeshroomDFM is a Meshroom Node that employs a Convolutional Neural Network to generate and refine feature matches between multiple images.
The goal of this project is to replace the classical Photogrammetry Pipeline Nodes for Feature Extraction, Image Matching and Feature Matching with an all-in-one solution.
Since Developer Documentation for creating custom Meshroom Nodes is hard to come by, the documentation for this project also demonstrates how to build and deploy binaries build with python and pyinstaller.

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

  You can simply install the precompiled binaries for linux in the <a href="#installation">Installation</a> step.
  If you wish to build the binaries yourself, follow <a href="#building-from-source">Building from Source</a>

### Installation

  * download the precompiled binaries for Linux

  * copy the binaries into the Meshroom binaries directory 
    ```sh
    cp dist path/to/bin
    ```

  * download the Mehsroom Nodes

  * copy the nodes into the Meshroom nodes directory
    ```sh
    cp nodes path/to/nodes
    ```


### Building from Source

  To build the binaries yourself, you can use pyinstaller to export the project.

  > **Note**
  > Pyinstaller only allows to build binaries for the platform you're running on.
  > If you wish to build the binaries for windows, you will have to execute pyinstaller on a windows machine.

  * Creating a new virtual environment

    It is recommended to create a virtual environment with the required packages
    ```sh
    conda env create -f environment.yml
    ```

  * Execute pyinstaller to build binaries
    ```sh
    pyinstaller dfm_wrapper.spec --onefile      # build the Deep Feature Matching Program
    pyinstaller dfm_analyzer.spec --onefile     # build Deep Feature Matching Analyzer
    ```

  * After building the binaries, you can continue with the installation steps 3 and 4

  <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Implementing the DFM Node

  * start Meshroom

  * right click and type "DeepFeatureMatching" to add the Deep Feature Matching Node

  * The node has inputs and outputs. Connect them as follows.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- PICTURES AND VIDEOS -->
<!-- ## Pictures and Videos


<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


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
* [DFM: A Performance Baseline for Deep Feature Matching](https://github.com/ufukefe/DFM)
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
[dfm]: https://github.com/ufukefe/DFM

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