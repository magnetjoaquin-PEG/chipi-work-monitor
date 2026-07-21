class SharePointService:

    @staticmethod
    def get_status():

        return {
            "connector": "graph",
            "status": "pending-approval",
            "site": "Generacionelica"
        }

    @staticmethod
    def get_inventory():

        documents = [
            {
                "name": "Procedimiento LOTO.pdf",
                "path": "/HSE/Procedimientos",
                "status": "ACTIVE"
            },
            {
                "name": "Auditoria_Interna_2026.docx",
                "path": "/Auditorias",
                "status": "ACTIVE"
            },
            {
                "name": "Plan_Accion_2026.xlsx",
                "path": "/Acciones",
                "status": "ACTIVE"
            }
        ]

        return {
            "total_documents": len(documents),
            "documents": documents
        }