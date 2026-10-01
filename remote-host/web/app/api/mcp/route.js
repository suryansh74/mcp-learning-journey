import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

export const dynamic = "force-dynamic";

function textOf(result) {
  const parts = (result.content || [])
    .map((block) => block.text)
    .filter(Boolean);
  if (parts.length) return parts.join("\n");
  return result.structuredContent ?? result;
}

function resourceText(result) {
  return (result.contents || []).map((block) => block.text ?? JSON.stringify(block));
}

async function withClient(fn) {
  const url = process.env.MCP_SERVER_URL;
  if (!url) {
    throw new Error("Set MCP_SERVER_URL to the tunnel or IP URL, including /mcp");
  }

  const client = new Client({ name: "next-host", version: "0.1.0" });
  const transport = new StreamableHTTPClientTransport(new URL(url));
  await client.connect(transport);
  try {
    return await fn(client);
  } finally {
    await client.close();
  }
}

export async function POST(request) {
  try {
    const body = await request.json();

    if (body.action === "list") {
      const tools = await withClient(async (client) => {
        const listed = await client.listTools();
        return listed.tools.map((tool) => ({
          name: tool.name,
          description: tool.description,
        }));
      });
      return Response.json({ url: process.env.MCP_SERVER_URL, tools });
    }

    if (body.action === "resources") {
      const resources = await withClient(async (client) => {
        const listed = await client.listResources();
        return listed.resources.map((resource) => ({
          uri: resource.uri,
          name: resource.name,
          description: resource.description,
        }));
      });
      return Response.json({ resources });
    }

    if (body.action === "read") {
      const result = await withClient((client) =>
        client.readResource({ uri: body.uri })
      );
      return Response.json({ uri: body.uri, text: resourceText(result) });
    }

    if (body.action === "call") {
      const result = await withClient((client) =>
        client.callTool({
          name: body.name,
          arguments: body.arguments || {},
        })
      );
      return Response.json({
        isError: result.isError,
        text: textOf(result),
      });
    }

    return Response.json(
      { error: "action must be list, resources, read, or call" },
      { status: 400 }
    );
  } catch (error) {
    return Response.json({ error: String(error) }, { status: 500 });
  }
}
