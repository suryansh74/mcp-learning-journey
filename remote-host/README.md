# Remote MCP host

Two pieces:

- `server/` — Python MCP server in Docker. Speaks Streamable HTTP on port 8000.
- `web/` — Next.js host. Its server route is the MCP client.

No login yet.

## One command

From `remote-host/`:

```bash
git pull
docker compose up --build
```

Then open http://localhost:3000.

You do not need `npm run dev`. The `web` container is the Next.js app. It calls the MCP server at `http://mcp:8000/mcp` on the Compose network, so you do not paste a URL.

- UI: http://localhost:3000
- MCP on this machine: http://localhost:8000/mcp
- Public MCP URL: the `https://....trycloudflare.com` line in the `tunnel` logs, plus `/mcp`

The tunnel is only for a client that is not in this Compose file. Stop it with Compose when you are done. A new run gets a new tunnel hostname.

## What replaces ngrok

Docker publishes port 8000 on your machine. That is a LAN address, not a public one.

The `tunnel` service is the ngrok stand-in (`cloudflared`, no account). Caddy is not here. Caddy is a reverse proxy that terminates HTTPS for a domain you already own.
