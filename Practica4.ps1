#Este script checa si los servicios que le proporcionas con un txt estan corriendo
#Para que funcione le debes de proporcionar el path del txt y el de donde quieres guardar la respuesta


function ver-servicios{
    param([Parameter(Mandatory)] [string] $path,
        [Parameter(Mandatory)][string]$respuesta)
    
    foreach($line in Get-Content -Path $path){
        $servicio = Get-Service -Name $line
        if($servicio.Status -eq "Running"){
            Add-Content -Path $respuesta -Value "Este servicio esta activo: $line " 
        }
    }
    Get-Content -Path $respuesta | Sort-Object
}
ver-servicios