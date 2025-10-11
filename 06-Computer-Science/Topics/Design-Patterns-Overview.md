# Design Patterns Overview

## 📋 Overview

**Topic**: Common Design Patterns in Software Development  
**Category**: Software Architecture  
**Level**: Intermediate to Advanced  
**Prerequisites**: OOP knowledge, programming experience  
**Estimated Time**: 3-4 hours

---

## 🎯 What You'll Learn

- What design patterns are and why they exist
- The three main categories of patterns
- Common patterns and when to use them
- How to recognize patterns in existing code
- When NOT to use patterns

---

## 1. What are Design Patterns?

> "Design patterns are typical solutions to common problems in software design."

### Key Points

- **Reusable solutions** to recurring problems
- **Proven approaches** developed over time
- **Common vocabulary** for developers
- **Not code** - they're concepts and approaches

### The Gang of Four (GoF)

In 1994, four authors published "Design Patterns: Elements of Reusable Object-Oriented Software":
- Erich Gamma
- Richard Helm
- Ralph Johnson
- John Vlissides

This book cataloged 23 classic design patterns.

---

## 2. Categories of Design Patterns

### Creational Patterns
Deal with object creation mechanisms.

- Singleton
- Factory Method
- Abstract Factory
- Builder
- Prototype

### Structural Patterns
Deal with object composition and relationships.

- Adapter
- Decorator
- Facade
- Proxy
- Composite

### Behavioral Patterns
Deal with communication between objects.

- Observer
- Strategy
- Command
- Iterator
- State

---

## 3. Common Creational Patterns

### Singleton Pattern

**Purpose**: Ensure a class has only one instance.

**Use Case**: Database connections, logging, configuration.

**Python Example**:
```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize connection
            cls._instance.connected = True
        return cls._instance

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance
```

⚠️ **Warning**: Singletons can make testing difficult. Use sparingly.

### Factory Pattern

**Purpose**: Create objects without specifying exact class.

**Use Case**: Creating different types of objects based on input.

**Python Example**:
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Usage
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # "Woof!"
```

### Builder Pattern

**Purpose**: Construct complex objects step by step.

**Use Case**: Objects with many optional parameters.

**Python Example**:
```python
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.vegetables = []

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self  # Return self for chaining
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_vegetables(self, veggies):
        self.pizza.vegetables.extend(veggies)
        return self
    
    def build(self):
        return self.pizza

# Usage - Method chaining
pizza = (PizzaBuilder()
         .set_size("large")
         .add_cheese()
         .add_pepperoni()
         .add_vegetables(["mushrooms", "olives"])
         .build())
```

---

## 4. Common Structural Patterns

### Adapter Pattern

**Purpose**: Make incompatible interfaces work together.

**Use Case**: Integrating third-party libraries with different interfaces.

**Python Example**:
```python
# Old interface
class OldPrinter:
    def print_document(self, text):
        print(f"[OLD] Printing: {text}")

# New interface expected by our code
class ModernPrinter:
    def print(self, text):
        pass

# Adapter
class PrinterAdapter(ModernPrinter):
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print(self, text):
        self.old_printer.print_document(text)

# Usage
old = OldPrinter()
adapter = PrinterAdapter(old)
adapter.print("Hello")  # Works with new interface!
```

### Decorator Pattern

**Purpose**: Add new functionality to objects dynamically.

**Use Case**: Adding features without modifying original class.

**Python Example**:
```python
# Python has built-in decorator syntax!

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"hello {name}"

print(greet("Alice"))  # "HELLO ALICE!!!"
```

### Facade Pattern

**Purpose**: Provide a simple interface to a complex system.

**Use Case**: Simplifying complex libraries or subsystems.

**Python Example**:
```python
# Complex subsystems
class DVDPlayer:
    def on(self): print("DVD Player on")
    def play(self): print("Playing DVD")

class Projector:
    def on(self): print("Projector on")
    def wide_screen_mode(self): print("Wide screen mode")

class SoundSystem:
    def on(self): print("Sound system on")
    def set_volume(self, level): print(f"Volume: {level}")

# Facade - simple interface
class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projector = Projector()
        self.sound = SoundSystem()
    
    def watch_movie(self):
        print("Get ready to watch a movie...")
        self.dvd.on()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound.on()
        self.sound.set_volume(5)
        self.dvd.play()

# Usage - one simple call instead of many
theater = HomeTheaterFacade()
theater.watch_movie()
```

---

## 5. Common Behavioral Patterns

### Observer Pattern

**Purpose**: Define one-to-many dependency between objects.

**Use Case**: Event handling, notifications, pub/sub systems.

**Python Example**:
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")

# Usage
subject = Subject()
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello observers!")
# Observer 1 received: Hello observers!
# Observer 2 received: Hello observers!
```

### Strategy Pattern

**Purpose**: Define a family of algorithms and make them interchangeable.

**Use Case**: Different ways to perform the same task.

**Python Example**:
```python
from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with credit card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with PayPal")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with cryptocurrency")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
        self.amount = 0
    
    def checkout(self):
        self.payment_strategy.pay(self.amount)

# Usage
cart = ShoppingCart(CreditCardPayment())
cart.amount = 100
cart.checkout()  # Paid $100 with credit card

# Switch strategy
cart.payment_strategy = PayPalPayment()
cart.checkout()  # Paid $100 with PayPal
```

### Command Pattern

**Purpose**: Encapsulate a request as an object.

**Use Case**: Undo/redo, macro recording, transaction management.

**Python Example**:
```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light is ON")
    
    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.history = []
    
    def execute_command(self, command):
        command.execute()
        self.history.append(command)
    
    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()

# Usage
light = Light()
light_on = LightOnCommand(light)

remote = RemoteControl()
remote.execute_command(light_on)  # Light is ON
remote.undo_last()  # Light is OFF
```

---

## 6. When to Use Design Patterns

### ✅ Use Patterns When:

1. **Problem is common** and pattern is proven
2. **Code is getting complex** and pattern simplifies it
3. **Team understands** the pattern
4. **Future flexibility** is needed

### ❌ Don't Use Patterns When:

1. **Simple solution works** - don't over-engineer
2. **You're learning** - understand problem first
3. **Forced fit** - pattern doesn't match problem
4. **Premature optimization** - YAGNI (You Aren't Gonna Need It)

---

## 7. Anti-Patterns to Avoid

### God Object
One class that does everything.

### Spaghetti Code
Tangled, unstructured code.

### Copy-Paste Programming
Duplicating code instead of abstracting.

### Golden Hammer
Using your favorite pattern for everything.

### Premature Optimization
Optimizing before knowing it's needed.

---

## 8. Pattern Recognition

### In Python Standard Library

**Iterator Pattern**:
```python
for item in my_list:  # Iterator pattern!
    print(item)
```

**Decorator Pattern**:
```python
@property  # Decorator pattern!
def name(self):
    return self._name
```

**Singleton Pattern**:
```python
import logging
logger = logging.getLogger()  # Singleton!
```

**Factory Pattern**:
```python
dict()  # Dictionary factory
list()  # List factory
```

### In Popular Frameworks

- **Django**: Observer (signals), Template Method
- **Flask**: Decorator, Factory
- **React**: Observer (hooks), Composite (components)

---

## 9. Quick Reference

| Pattern | Purpose | Common Use Case |
|---------|---------|-----------------|
| **Singleton** | One instance only | Database connection |
| **Factory** | Create objects | Object creation based on input |
| **Builder** | Construct complex objects | Objects with many parameters |
| **Adapter** | Interface compatibility | Third-party integration |
| **Decorator** | Add functionality | Extending classes |
| **Facade** | Simplify interface | Complex system wrapper |
| **Observer** | Event notification | Event systems |
| **Strategy** | Interchangeable algorithms | Different implementations |
| **Command** | Encapsulate requests | Undo/redo functionality |

---

## 10. Learning Path

### Beginner
1. Understand the problem patterns solve
2. Learn 3-5 most common patterns
3. Recognize patterns in existing code

### Intermediate
1. Implement patterns in your projects
2. Learn remaining GoF patterns
3. Understand pattern trade-offs

### Advanced
1. Combine patterns effectively
2. Know when NOT to use patterns
3. Create your own patterns

---

## 📚 Resources

### Books
- **"Design Patterns"** - Gang of Four (Classic but dense)
- **"Head First Design Patterns"** - Freeman & Robson (Beginner-friendly)
- **"Python Design Patterns"** - Gennadiy Zlobin

### Online
- [Refactoring.Guru](https://refactoring.guru/design-patterns) - Excellent visual guides
- [Source Making](https://sourcemaking.com/design_patterns) - Clear explanations
- [Python Patterns](https://python-patterns.guide/) - Python-specific

### Videos
- Christopher Okhravi - Design Patterns Series
- Derek Banas - Design Pattern Tutorials

### Practice
- Implement each pattern yourself
- Find patterns in open-source projects
- Refactor existing code to use patterns

---

## 🎯 Exercise

### Challenge: Refactor with Patterns

Take this code and apply appropriate patterns:

```python
class App:
    def run(self):
        # Connect to database
        db_host = "localhost"
        db_port = 5432
        # ... 20 lines of connection code ...
        
        # Get user input
        # ... validation code ...
        
        # Process data
        # ... 50 lines of logic ...
        
        # Generate report
        # ... another 30 lines ...
        
        # Send email
        # ... email code ...
```

**Which patterns could help?**
- Facade (database connection)
- Strategy (different processing methods)
- Command (operations)
- Builder (report generation)

---

## 💡 Final Thoughts

1. **Patterns are tools**, not rules
2. **Simple first**, pattern later if needed
3. **Understand the problem** before applying pattern
4. **Communicate**: Use pattern names with team
5. **Practice**: Implement patterns to learn them

---

**Remember**: "A pattern is a solution to a problem in a context." Make sure all three align before using a pattern!

