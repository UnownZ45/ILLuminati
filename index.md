# ILLuminati

*Project is still in development*

Use at your own discretion.


## About This Project

Hey there, we are so glad you found us, we are *ILLuminati*. ILLuminati is a starting business that is combining LED technology with cars to bring a cheaper and better under-glow option to cars. This specific project focuses only on under-glow but [here](https://www.github.com) is where you'll be able to access our interior lighting program.


## How to Use

This project is extremely easy to use simply just
- Download or Clone the files from this repository
  - You can also visit [releases]() and download the files there
- Modify the code to your needs
  - In the main.py file you will want to set your switch pinouts to fit your needs
  - In the slavescripts.py file you can add more colors or color schemes for a full custom experience (just be sure you reference those colors in the main.py file)
  - To generate color presets run the Color_Generation.py and input a hexidecimal color and it will return the RGB value needed in the main.py or slavescripts.py
- load the main.py and slavescripts.py files onto you Raspberry Pi Pico (or Micro Controller of you choice (we have only tested with the RP2040 chipset though))
- BAM! You can now install your switches and lights to your Pico and car to bask in it's renewed gloriousness


## Features (both present and future)
Since this project is still a work in progress we still have plans to further improve. Plans are as follows

*in testing phase*

- [ ] *Basic functionality*
- [ ] *An Assortment of easy-to-load color presets for easy customization*
- [ ] An Assortment of multicolor and moving color presets for cooler customization
- [ ] Merging interior lighting with under-glow for the best custom lighting for you vehicle
- [ ] Phone Linking to allow for mobile control
- [ ] Use of Potentiometer for brightness control
- [ ] Use of Potentiometer for color control
