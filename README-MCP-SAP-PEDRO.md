# MCP SAP Pedro

Configuração baseada no [ARC-1](https://github.com/arc-mcp/arc-1) para conectar ferramentas MCP a sistemas SAP ABAP.

## Configuração

Defina as variáveis de ambiente no ambiente de desenvolvimento:

- `SAP_URL`
- `SAP_USER`
- `SAP_PASSWORD` (secreta)
- `SAP_CLIENT` (padrão: `100`)
- `SAP_LANGUAGE` (padrão: `EN`)
- `SAP_INSECURE` (padrão: `false`)
- `SAP_ALLOW_WRITES` (padrão: `false`)

A configuração usa `npx -y arc-1@latest` e mantém mutações SAP desabilitadas por padrão.

## Execução

Use `mcp.json` como configuração do cliente MCP. Nunca commite senhas, tokens ou URLs com credenciais.
