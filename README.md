# Parent Me
Welcome to the Child Adoption Assistance Project! Our goal is to provide a platform that assists parents in the adoption process by offering comprehensive documentation guidance and a crowdfunding option to help raise funds for noble causes.

This project aims to simplify the adoption procedure, ensuring that parents have access to the necessary information and resources. Additionally, the crowdfunding feature enables users to create campaigns to support others in their adoption journey.

## Table of Contents
- Introduction
- Features
- Tech Stacks
- Installation
- Usage
- Contributing
- License


## Features
- **Adoption Documentation Assistance**: Detailed documentation and step-by-step guides to help parents navigate the adoption process seamlessly.

- **Crowdfunding Platform**: Users can create crowdfunding campaigns to raise funds for adoption-related expenses, facilitating financial support for those in need.

- **Transparent and Secure**: Leveraging blockchain technology to ensure transparency and security in the crowdfunding process, providing users with a trustworthy platform.

- **Multi-tech Integration**: The project incorporates a variety of technologies, including HTML, CSS, JavaScript, Node.js, Solidity, Blockchain, PHP, React, and Django.

## Tech Stacks
- Frontend:
  - HTML
  - CSS
  - JavaScript
  - React

- Backend:
  - Node.js
  - Django
  - PHP
- Blockchain:
  - Solidity
  - Blockchain (Integrated for secure and transparent crowdfunding)

# Installation

### Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

### Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:

```
git clone https://github.com/your-name/ParentMe.git
```

where `your-name` is your GitHub username. Here you're copying the contents of the Parent Me repository from GitHub to your computer.


### Navigate to the project directory:


```
cd ParentMe
```
### To Run the Website and BackEnd
Your System must have
- Django
- Pillow

If not Installed these, run the following Commands in CMD one by one
```
pip install django
pip install Pillow
```
After that Open the repository in Code Editor and navigate to the following directory:
```
cd backend
```
After that 
```
python manage.py create superuser
```
Now, to Create SuperUser , you will be asked to enter `username`, `email`(optional),`password` and `Confirm Password`. 
After Entering the details 

```
python manage.py makemigrations
python manage.py migrate
```
### To Run the BlockChain
Your System Must have `NodeJs`.
After that , return to the `ParentMe` Folder by running the following command till `ParentMe` has reached:
```
cd ..
```
Now Run the commands one by one:
```
cd client
npx thirdweb create --template vite-javascript-starter
npm i yarn
npm run deploy
npm run dev
```
The Server will start at `http://localhost:5173/`.
No need of opening the server, it will open when you Pay in the Donate Page of Main Website

**Note :** To make Campagion, you will be required to create a MetaMask([Click to Download and SignUp](https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn)) or any BitCoin Wallet Account.

After that, when you open the Campagion Page, Click on `Connect` on top right page and msut open the window in the browser in which you have created the MetaMask Accoont.

### To Run UPI Part
You will be required to Run the XAMPP Server([Click to Download](https://www.apachefriends.org/download.html))
There will be two Files in the Repo named `index.php` and `success.php`. 
Move these files into the directory as
```
C->Xampp->htdocs
```
After that create a folder named `phonepe` and paste both the files in it then run the server using `XAMPP Control Pannel`.

**Now You Are all Se to Use Our Website. Enjoy !!**

### How to Create Campagions
- To create a crowdfunding campaign, log in as stated in above steps and visit the crowdfunding platform. Follow the steps to set up your campaign and share it with others.

- Explore and contribute to ongoing crowdfunding campaigns to support fellow users in their adoption journey.

# Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow the General Contribution Guidelines.
