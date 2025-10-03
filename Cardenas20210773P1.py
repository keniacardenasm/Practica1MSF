"""
Práctica 1: Diseño de Controlador para un Sistema de Segundo Orden

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Kenia cardenas manzo
Número de control: 20210773
Correo institucional: kenia.cardenas201@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,7,3.5 
n = round((tend-t0)/dt)+1
t = np.linspace(t0,tend,n)
u1 = np.ones(n)
u2 = np.zeros(n); u2[round(1/dt):round(2/dt)]=1
u3 = t/tend
u4 = np.sin(m.pi/2*t)

# Componentes del circuito RLC y función de transferencia
R,L,C = 22E3,220E-6,10E-6
num = [C*L*R,C*R**2+L,R]
den = [3*C*L*R,5*C*R**2+L,2*R]
L = np.roots(den)
print(f"las raices son {L[0]} y {L[1]}")
sys = ctrl.tf(num,den)
print(f"funcion de transferencia del sistema: {sys}")

# Componentes del controlador
kI= 6547.87290036297
Cr = 1E-6
Re = 1/(kI*Cr)

print(f"el valor de la capacitancia propuesta de Cr es de {Cr} Faradios")
print(f"el valor de la resistencia de Re {Re} ohms")

numPID = [1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID,denPID)
print(f"La funcion de transferencia del controlador I es {PID}")

# Sistema de control en lazo cerrado
x = ctrl.series(PID,sys)
sysPID = ctrl.feedback(x,1,sign = -1)
print(f"Funciion de transferencia del sistema de control en lazo cerrado {sysPID}")

# Respuesta del sistema en lazo abierto y en lazo cerrado
clr1 = np.array([119,190,240])/255
clr2 = np.array([255,203,97])/255
clr6 = np.array([6,66,50])/255

_,Vsu1 = ctrl.forced_response(sys,t,u1,x0)
_,Vsu2 = ctrl.forced_response(sys,t,u2,x0)
_,Vsu3 = ctrl.forced_response(sys,t,u3,x0)
_,Vsu4 = ctrl.forced_response(sys,t,u4,x0)

_,pidu1 = ctrl.forced_response(sysPID,t,u1,x0)
_,pidu2 = ctrl.forced_response(sysPID,t,u2,x0)
_,pidu3 = ctrl.forced_response(sysPID,t,u3,x0)
_,pidu4 = ctrl.forced_response(sysPID,t,u4,x0)

fg1 = plt.figure() 
plt.plot(t,u1,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,Vsu1,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pidu1,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi[s]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center',ncol = 3,
           fontsize = 9, frameon = True)
plt.show()
fg1.savefig('step_python.pdf',bbox_inches = 'tight')

fg2 = plt.figure() 
plt.plot(t,u2,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,Vsu2,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pidu2,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi[s]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center',ncol = 3,
           fontsize = 9, frameon = True)
plt.show()
fg2.savefig('impulso_python.pdf',bbox_inches = 'tight')

fg3 = plt.figure() 
plt.plot(t,u3,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,Vsu3,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pidu3,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi[s]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center',ncol = 3,
           fontsize = 9, frameon = True)
plt.show()
fg3.savefig('Rampa_python.pdf',bbox_inches = 'tight')

fg4 = plt.figure() 
plt.plot(t,u4,'-',color = clr1,label = 'Ve(t)')
plt.plot(t,Vsu4,'--',color = clr2,label = 'Vs(t)')
plt.plot(t,pidu4,':',linewidth = 4,color = clr6,label = 'PID(t)')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-1.2,1.2); plt.yticks(np.arange(-1.2,1.3,0.2))
plt.xlabel('t[s]',fontsize = 11)
plt.ylabel('Vi[s]',fontsize = 11)
plt.legend(bbox_to_anchor = (0.5,-0.2),loc = 'center',ncol = 3,
           fontsize = 9, frameon = True)
plt.show()
fg4.savefig('Senoidal_python.pdf',bbox_inches = 'tight')