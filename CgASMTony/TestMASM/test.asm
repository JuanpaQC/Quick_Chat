INCLUDE Irvine32.inc

.DATA
fileName BYTE  "C:\Users\jpqca\OneDrive\Escritorio\Recibidos\mensajes_recibidos.txt", 0
buffer BYTE 5000 DUP(0)
previousFileSize DWORD 0
currentFileSize DWORD 0
fileHandle HANDLE ?

.CODE
main PROC 
    ; Abrir el archivo
    mov edx, OFFSET fileName 
    call OpenInputFile 
    mov [fileHandle], eax   ; Guardar el handle del archivo

readLoop:
    ; Leer el contenido del archivo
    mov edx, OFFSET buffer 
    mov ecx, SIZEOF buffer 
    call ReadFromFile 

    ; Calcular el tamaño actual del archivo
    mov eax, currentFileSize
    add eax, ecx            ; Suma el tamaño leído al tamaño actual
    mov [currentFileSize], eax

    ; Verificar si ha habido cambios en el archivo
    mov eax, [previousFileSize]
    cmp eax, [currentFileSize]  ; Compara el tamaño anterior con el actual
    je noChanges                ; Si son iguales, no hay cambios, salta a noChanges
    mov [previousFileSize], eax ; Actualiza el tamaño anterior

    ; Mostrar el contenido del archivo
    mov edx, OFFSET buffer 
    call WriteString 
    call Crlf

noChanges:
    ; Esperar un momento antes de verificar nuevamente
    mov eax, 1000           ; Espera 1 segundo
    call Sleep

    jmp readLoop            ; Vuelve a leer el archivo

endProgram:
    ; Cerrar el archivo
    mov eax, [fileHandle]
    call CloseFile 

    call Crlf
    exit
main ENDP 

END main
