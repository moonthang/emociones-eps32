import cv2
from deepface import DeepFace

# Inicializar la webcam
cap = cv2.VideoCapture(0)

print("Iniciando reconocimiento de emociones. Presiona 'q' para salir.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la webcam.")
        break

    try:
        # Analizar el fotograma actual en busca de emociones
        resultado = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        
        # Obtener la emoción dominante
        emocion_dominante = resultado[0]['dominant_emotion']
        
        # Mostrar la emoción en la consola de la PC
        print(f"Emoción detectada: {emocion_dominante}")

        # Dibujar la emoción en la ventana de video de la PC
        cv2.putText(frame, f"Emocion: {emocion_dominante}", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    except Exception as e:
        # Si hay algún error procesando el frame, continúa
        pass

    # Mostrar la ventana de la cámara
    cv2.imshow('Reconocimiento de Emociones - PC', frame)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()