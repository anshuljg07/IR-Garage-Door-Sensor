# Garage Door Sensor
![Passing](https://github.com/matplotlib/matplotlib/workflows/Tests/badge.svg)
![CodeQl Passing](https://github.com/tesseract-ocr/tesseract/workflows/CodeQL/badge.svg)
![Passing](https://camo.githubusercontent.com/0029e047a1f03572a4cc1d1f390606028f57cf6faa8cfa2f999798920970c362/68747470733a2f2f63692e6170707665796f722e636f6d2f6170692f70726f6a656374732f7374617475732f6d69616830696b667366306a333831392f6272616e63682f6d61737465723f7376673d74727565)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<img width="464" alt="Garagedoorsensorschematic" src="https://github.com/anshuljg07/IR-Receiver/assets/72891464/67b5e9da-26fd-42bc-997e-31ac303c53f3">
<p>
We designed and implementing an “electric eye” light beam-interrupter safety system, as seen above, is composed of two components: the transmitter (Tx) and the receiver (Rx). The Tx must produce a modulated transmit beam, and the Rx must detect, filter, and amplify the signal. Thus, with this information the Rx must determine whether the Rx is out of range of Tx’s transmit beam or if the Tx is not transmitting, and if so, it must send a text notification to the user.
</p>

### IR Transmitter Schematic
<img width="473" alt="TransmitterSchematic" src="https://github.com/anshuljg07/IR-Receiver/assets/72891464/74857232-7b41-4956-a258-968069bbe362">
<p>
<br />
The transmitter consists of a ICM7555IPAZ CMOS 555 timer, which produces a consistent square wave. The frequency of the transmitter is configured to 534 Hz. The signal generated is then transmitted using LTE-5228A.
  
</p>


### Receiver Transmitter Schematic:
<img width="473" alt="HighLevelReceiver" src="https://github.com/anshuljg07/IR-Receiver/assets/72891464/f835b47b-066d-4c5e-9eb2-ca894d4afe44">
<p>
  <br />
The receiver consists of multiples encapsulated stages designed for specific functions. The first stage is the IR photodiodes, which read in the transmitted signal. Then they are fed into a high pass buffer, designed to isolate the transmitter's IR signal and filter out any noise from ambient light. Then a buffer is implemented to prevent surges of current from overloading the downstream components, mainly the raspberry pi. Then the signal is fed into an amplifier designed to increase gain and maximize the receiver's receiving distance. Next a peak detector captures the peak of the AC IR signal. Then the ADC converts the signal into a DC signal that can be registered by the Raspberry Pi's GPIO pins. 
</p>
<p>
  <br />
From here there is a shift from hardware to software, where a python script local to the Pi constantly polls the state of the ADC output. If it is low, then no signal is detected by the receiver so an email is sent. We make use of the SendinBlue RESTFul API python wrapper, sib-api-v3-sdk, to send transactional emails. The contents of the email were organized to follow the requirements dictated by Simple Mail Transfer Protocol. This email object was then sent along with an API key provided by the Brevo SMTP service.
</p>

## Contributors
This project was developed and is currently maintained by Rafael Ragel de la Tejera, Anshul Gowda, and Joseph Bartosyck.

## Get in Contact:
 [Anshul Gowda's LinkedIn](https://www.linkedin.com/in/anshul-gowda)
<br />
Rafael Rangel de la Tejera's LinkedIn
<br />
Joseph Bartosyck's de la Tejera's LinkedIn
