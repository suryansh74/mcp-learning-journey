# Remote MCP host

Two pieces:

- `server/` — Python MCP server in Docker. Speaks Streamable HTTP on port 8000.
- `web/` — Next.js host. Its server route is the MCP client. It connects to `MCP_SERVER_URL`.

No login yet. Paste a URL, then call tools.

## What replaces ngrok

Docker alone only publishes a port on the machine it runs on (`http://YOUR_IP:8000/mcp`). That IP works on your LAN. It is not a public internet address.

The `tunnel` service is the ngrok stand-in. It is `cloudflared` with a free quick tunnel (no account, no custom domain). When it starts, the logs print a public `https://....trycloudflare.com` URL. Copy that and add `/mcp`.

Caddy is not in this setup. Caddy is a reverse proxy that terminates HTTPS for a domain you already own. Use it later, on the Oracle VM, when you have a real domain.

## Run the server and the tunnel

```bash
cd remote-host
docker compose up --build mcp tunnel
```

In the `tunnel` logs, find a line like:

```text
https://something-random.trycloudflare.com
```

The MCP URL is that host plus `/mcp`:

```text
https://something-random.trycloudflare.com/mcp
```

LAN-only alternative (no tunnel): `http://YOUR_LAN_IP:8000/mcp`

## Point the Next.js client at it

```bash
cd web
cp .env.example .env.local
# set MCP_SERVER_URL to the URL you copied
npm install
npm run dev
```

Open http://localhost:3000. The page lists tools and can call `add_numbers` and `say_hello`.

`MCP_SERVER_URL` is read on the server, not in the browser. Restart `npm run dev` after you change it.

## Run the web app in Docker too

```bash
# from remote-host/, after you know the public URL
MCP_SERVER_URL=https://something-random.trycloudflare.com/mcp docker compose up --build web
```

If the web container is on the same Compose network and you do not need a public URL, leave the default: `http://mcp:8000/mcp`.
