# totp
Timed One Time Password (totp) allows you to provide QR Code secret and it will give you a one time password that expires every 30 seconds. This is a great way to verify or login into your account as a two factor authentication method if you dont have your google authenticator on you, but have your QR code secret.


Run code and provide QR code secret
  ```
  $ totp-code.py <base32_QRcode>
  ```

