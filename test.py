import tkinter as tk
import random
import math
from abc import ABC, abstractmethod
from typing import List, Dict, Type

# ============================================================================
# OBJECT SYSTEM - Base Classes
# ============================================================================

class GameObject(ABC):
    """Abstract base class for all game objects"""
    _id_counter = 0
    
    def __init__(self, x: float, y: float):
        self.id = GameObject._id_counter
        GameObject._id_counter += 1
        self.x = x
        self.y = y
        self.active = True
    
    @abstractmethod
    def update(self, dt: float, canvas_width: int, canvas_height: int):
        """Update object state"""
        pass
    
    @abstractmethod
    def draw(self, canvas: tk.Canvas):
        """Draw object on canvas"""
        pass
    
    @abstractmethod
    def get_type_name(self) -> str:
        """Return the type name of this object"""
        pass


# ============================================================================
# CONCRETE OBJECT TYPES
# ============================================================================

class Particle(GameObject):
    """Base particle class with physics"""
    def __init__(self, x: float, y: float, vx: float, vy: float, color: str, size: int):
        super().__init__(x, y)
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.gravity = 0.3
        self.bounce = 0.7
    
    def update(self, dt: float, canvas_width: int, canvas_height: int):
        # Apply gravity
        self.vy += self.gravity
        
        # Update position
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x - self.size < 0 or self.x + self.size > canvas_width:
            self.vx *= -self.bounce
            self.x = max(self.size, min(canvas_width - self.size, self.x))
        
        if self.y + self.size > canvas_height:
            self.vy *= -self.bounce
            self.y = canvas_height - self.size
            
            # Remove if stopped bouncing
            if abs(self.vy) < 0.5:
                self.active = False
        
        # Remove if off screen top
        if self.y < -50:
            self.active = False


class CircleParticle(Particle):
    """Circle shaped particle"""
    def draw(self, canvas: tk.Canvas):
        canvas.create_oval(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color, outline=""
        )
    
    def get_type_name(self) -> str:
        return "Circle"


class SquareParticle(Particle):
    """Square shaped particle"""
    def draw(self, canvas: tk.Canvas):
        canvas.create_rectangle(
            self.x - self.size, self.y - self.size,
            self.x + self.size, self.y + self.size,
            fill=self.color, outline=""
        )
    
    def get_type_name(self) -> str:
        return "Square"


class TriangleParticle(Particle):
    """Triangle shaped particle"""
    def draw(self, canvas: tk.Canvas):
        points = [
            self.x, self.y - self.size,
            self.x - self.size, self.y + self.size,
            self.x + self.size, self.y + self.size
        ]
        canvas.create_polygon(points, fill=self.color, outline="")
    
    def get_type_name(self) -> str:
        return "Triangle"


class StarParticle(Particle):
    """Star shaped particle"""
    def draw(self, canvas: tk.Canvas):
        points = []
        for i in range(10):
            angle = (i * 36 - 90) * math.pi / 180
            radius = self.size if i % 2 == 0 else self.size * 0.4
            points.extend([
                self.x + radius * math.cos(angle),
                self.y + radius * math.sin(angle)
            ])
        canvas.create_polygon(points, fill=self.color, outline="")
    
    def get_type_name(self) -> str:
        return "Star"


class Emitter(GameObject):
    """Emits particles continuously"""
    def __init__(self, x: float, y: float, particle_type: Type[Particle], rate: int = 5):
        super().__init__(x, y)
        self.particle_type = particle_type
        self.rate = rate
        self.counter = 0
        self.particles_created = 0
    
    def update(self, dt: float, canvas_width: int, canvas_height: int):
        self.counter += 1
    
    def draw(self, canvas: tk.Canvas):
        # Draw emitter as a small square
        canvas.create_rectangle(
            self.x - 5, self.y - 5,
            self.x + 5, self.y + 5,
            fill="white", outline="black"
        )
    
    def get_type_name(self) -> str:
        return "Emitter"
    
    def should_emit(self) -> bool:
        return self.counter % self.rate == 0
    
    def create_particle(self) -> Particle:
        """Create a new particle"""
        vx = random.uniform(-3, 3)
        vy = random.uniform(-10, -5)
        color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink"])
        size = random.randint(5, 15)
        self.particles_created += 1
        return self.particle_type(self.x, self.y, vx, vy, color, size)


# ============================================================================
# OBJECT MANAGER
# ============================================================================

class ObjectManager:
    """Manages all game objects with efficient storage and retrieval"""
    def __init__(self):
        self.objects: List[GameObject] = []
        self.objects_by_type: Dict[str, List[GameObject]] = {}
        self.emitters: List[Emitter] = []
    
    def add_object(self, obj: GameObject):
        """Add an object to the manager"""
        self.objects.append(obj)
        
        # Add to type dictionary
        type_name = obj.get_type_name()
        if type_name not in self.objects_by_type:
            self.objects_by_type[type_name] = []
        self.objects_by_type[type_name].append(obj)
        
        # Track emitters separately
        if isinstance(obj, Emitter):
            self.emitters.append(obj)
    
    def update_all(self, dt: float, canvas_width: int, canvas_height: int):
        """Update all objects and handle emitters"""
        # Update existing objects
        for obj in self.objects:
            obj.update(dt, canvas_width, canvas_height)
        
        # Handle emitters creating new particles
        for emitter in self.emitters:
            if emitter.active and emitter.should_emit():
                particle = emitter.create_particle()
                self.add_object(particle)
        
        # Remove inactive objects
        self.cleanup_inactive()
    
    def cleanup_inactive(self):
        """Remove inactive objects from all collections"""
        # Remove from main list
        self.objects = [obj for obj in self.objects if obj.active]
        
        # Remove from type dictionary
        for type_name in self.objects_by_type:
            self.objects_by_type[type_name] = [
                obj for obj in self.objects_by_type[type_name] if obj.active
            ]
        
        # Remove from emitters list
        self.emitters = [e for e in self.emitters if e.active]
    
    def draw_all(self, canvas: tk.Canvas):
        """Draw all objects"""
        for obj in self.objects:
            obj.draw(canvas)
    
    def get_count_by_type(self, type_name: str) -> int:
        """Get count of objects of a specific type"""
        return len(self.objects_by_type.get(type_name, []))
    
    def get_total_count(self) -> int:
        """Get total object count"""
        return len(self.objects)
    
    def get_stats(self) -> Dict[str, int]:
        """Get statistics about all object types"""
        stats = {}
        for type_name, objs in self.objects_by_type.items():
            stats[type_name] = len(objs)
        return stats


# ============================================================================
# MAIN APPLICATION
# ============================================================================

class ParticleSimulation:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Particle Simulation - Object System Demo")
        
        # Canvas setup
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()
        
        # Object manager
        self.manager = ObjectManager()
        
        # Control panel
        self.setup_controls()
        
        # Bind mouse click
        self.canvas.bind("<Button-1>", self.on_click)
        
        # Current particle type
        self.particle_types = [CircleParticle, SquareParticle, TriangleParticle, StarParticle]
        self.current_type_index = 0
        
        # Start animation
        self.running = True
        self.animate()
    
    def setup_controls(self):
        """Setup control panel"""
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Info label
        self.info_label = tk.Label(control_frame, text="Click to spawn particles | Press SPACE to change type")
        self.info_label.pack(side=tk.LEFT)
        
        # Stats label
        self.stats_label = tk.Label(control_frame, text="Objects: 0")
        self.stats_label.pack(side=tk.RIGHT)
        
        # Type label
        self.type_label = tk.Label(control_frame, text="Type: Circle", font=("Arial", 12, "bold"))
        self.type_label.pack(side=tk.RIGHT, padx=10)
        
        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(btn_frame, text="Add Emitter", command=self.add_emitter).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Change Type (SPACE)", command=self.change_type).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=2)
        
        # Bind keyboard
        self.root.bind("<space>", lambda e: self.change_type())
    
    def on_click(self, event):
        """Handle mouse click to create particles"""
        for _ in range(10):  # Create 10 particles per click
            vx = random.uniform(-5, 5)
            vy = random.uniform(-15, -5)
            color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"])
            size = random.randint(5, 15)
            
            particle_class = self.particle_types[self.current_type_index]
            particle = particle_class(event.x, event.y, vx, vy, color, size)
            self.manager.add_object(particle)
    
    def add_emitter(self):
        """Add a new emitter at a random position"""
        x = random.randint(100, 700)
        y = random.randint(50, 200)
        particle_type = random.choice(self.particle_types)
        emitter = Emitter(x, y, particle_type, rate=random.randint(3, 10))
        self.manager.add_object(emitter)
    
    def change_type(self):
        """Change current particle type"""
        self.current_type_index = (self.current_type_index + 1) % len(self.particle_types)
        type_name = self.particle_types[self.current_type_index].__name__.replace("Particle", "")
        self.type_label.config(text=f"Type: {type_name}")
    
    def clear_all(self):
        """Clear all objects"""
        for obj in self.manager.objects:
            obj.active = False
        self.manager.cleanup_inactive()
    
    def animate(self):
        """Main animation loop"""
        if not self.running:
            return
        
        # Clear canvas
        self.canvas.delete("all")
        
        # Update and draw
        self.manager.update_all(1, 800, 600)
        self.manager.draw_all(self.canvas)
        
        # Update stats
        stats = self.manager.get_stats()
        stats_text = f"Total: {self.manager.get_total_count()} | "
        stats_text += " | ".join([f"{k}: {v}" for k, v in sorted(stats.items())])
        self.stats_label.config(text=stats_text)
        
        # Continue animation
        self.root.after(16, self.animate)  # ~60 FPS


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = ParticleSimulation(root)
    root.mainloop()