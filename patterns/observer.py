class AccountSubject: 
    def __init__(self): # constructor
        self._observers = [] # Observer list

    def attach(self, observer): # Attach observer
        self._observers.append(observer)  # Add observer to list

    def detach(self, observer): # Detach observer
        self._observers.remove(observer) # Remove observer from list

    def notify(self, message): # Notify observers
        for observer in self._observers: # Iterate over observers
            observer.update(message) # Update observer with message


class Observer:
    def update(self, message): # Update method
        pass


class LoggerObserver(Observer): # Logger observer
    def update(self, message): # Update method
        print(f"[Logger] {message}") # Print message with logger label

class NotificationObserver(Observer):
    def update(self, message):
        print(f"[Notification] {message}")
