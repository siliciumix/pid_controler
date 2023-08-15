import matplotlib.pyplot as plt
import time

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, current_value):
        error = setpoint - current_value

        # Proportional term
        proportional_term = self.kp * error

        # Integral term
        self.integral += error
        integral_term = self.ki * self.integral

        # Derivative term
        derivative_term = self.kd * (error - self.prev_error)
        self.prev_error = error

        # Compute control output
        control_output = proportional_term + integral_term + derivative_term

        return control_output

# Beispielwerte für die Reglerkonstanten
kp = 1.0
ki = 0.1
kd = 0.01

# Setpoint (gewünschter Wert) und initialer aktueller Wert
setpoint = 50.0
current_value = 30.0

# Regler-Objekt erstellen
pid_controller = PIDController(kp, ki, kd)

# Simulierte Werte speichern
simulated_values = []

# Zeitstempel speichern
timestamps = []

# Linien-Diagramm vorbereiten
plt.ion()  # Interaktiver Modus einschalten
fig, ax = plt.subplots()

# Regelschleife und Diagramm-Update
for i in range(100):
    control_output = pid_controller.compute(setpoint, current_value)
    
    # Simuliere eine Systemreaktion (hier wird der aktuelle Wert einfach erhöht)
    current_value += control_output
    
    # Simulierte Werte und Zeitstempel speichern
    simulated_values.append(current_value)
    timestamps.append(i)
    
    # Diagramm aktualisieren
    ax.clear()
    ax.plot(timestamps, simulated_values, label='Simulated Value')
    ax.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('PID Controller Simulation')
    ax.legend()
    plt.pause(0.1)  # Kurze Pause, um das Diagramm anzuzeigen

# Diagramm am Ende anzeigen
plt.ioff()
plt.show()
