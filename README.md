# car_monitor
Code to talk to ODBII bluetooth module based on ELM327 chip.

### Debuging

I used a RN42 on SPP profile + a FTDI board to get starting on this project since I did not know much about ODB, 
ODB protocol, etc.  This allowed me to simulate the ODB connector without having to experiment on the real thing
(since I did not want to have my car on run for an extended period of time)

References:
- [ELM327 datasheet](http://elmelectronics.com/DSheets/ELM327DS.pdf) / ELMElectronics \(R\)
- Sparkfun [ODB Hookup guide](https://learn.sparkfun.com/tutorials/obd-ii-uart-hookup-guide)
- Sparkfun [RN-42 based module](https://www.sparkfun.com/products/12576)  
- [An Introduction to Bluetooth Programming](http://people.csail.mit.edu/albert/bluez-intro)
- How to [enable bluetooth on boot](http://rwx.io/blog/2015/02/18/seting-up-an-edison/)