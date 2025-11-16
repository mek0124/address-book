# Address Book - Future Plan

### Version 1.2.0
  - incorporate a user profile. It's still local host, but gives it a more personal touch. It'll allow the user to enter their own information, customize the application anyway they see fit with color schemes and such to that nature and it'll allow for multi-user, same-device, usage

### Version 1.4.0
  - incorporate an update feature that checks the applications version against the version of the latest release on github. If they don't match -> prompt the user to update the files. If the user declines the update, continue running on the same version. 
  > NOTE: at some point, the current version will fade out as the updates roll out progressively. There will need to ***eventually*** be a check system so that if the user is on an unsupported version, then it will not allow them to use the application anymore until they at least agree to update to the oldest version on the supported list

### Version 2.0.0
  - migrate from `sqlite3` to `sqlalchemy` for more efficient relational database storage

### Version 3.0.0
  - migrate from `sqlalchemy` to an online database (no google or apple of any sorts if possible, **user privacy**) to allow online storage
  - incorporate authentication and security
  - start development on web version

### Version 
  - 1.0.0 - Mobile
    - direct copy of desktop version, but mobile friendly
    - likely expo as the framework
  - 3.2.0 - Desktop
    - migrate from PySide6 to Tauri application
    - migrate from internal mixed client/server logic to stand alone client-server partnership
    - start construction on FastAPI server

### Version
  - 1.2.0 - Mobile
    - fix bugs/issues
  - 3.4.0 - Desktop
    - move new contact form from landing screen behind button
    - create menu bar for application multi-page navigation
      - Contacts -> landing page
      - Profile -> user profile -> add/update/remove information or profile icon
      - Settings -> color schemes, animations (on/off), etc.