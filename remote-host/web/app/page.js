"use client";

import { useState } from "react";

export default function Home() {
  const [tools, setTools] = useState([]);
  const [log, setLog] = useState("");
  const [name, setName] = useState("say_hello");
  const [argsText, setArgsText] = useState('{"name":"Suryansh"}');
  const [busy, setBusy] = useState(false);

  async function callApi(body) {
    setBusy(true);
    try {
      const response = await fetch("/api/mcp", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(body),
      });
      const data = await response.json();
      setLog(JSON.stringify(data, null, 2));
      if (data.tools) setTools(data.tools);
    } catch (error) {
      setLog(String(error));
    } finally {
      setBusy(false);
    }
  }

  return (
    <main>
      <h1>Next.js MCP host</h1>
      <p>
        The browser talks to this app. This app talks to the MCP server URL in
        <code> MCP_SERVER_URL</code>.
      </p>
      <button disabled={busy} onClick={() => callApi({ action: "list" })}>
        List tools
      </button>
      <ul>
        {tools.map((tool) => (
          <li key={tool.name}>
            <button
              onClick={() => {
                setName(tool.name);
                setArgsText(
                  tool.name === "add_numbers"
                    ? '{"a":2,"b":3}'
                    : '{"name":"Suryansh"}'
                );
              }}
            >
              {tool.name}
            </button>{" "}
            {tool.description}
          </li>
        ))}
      </ul>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          callApi({
            action: "call",
            name,
            arguments: JSON.parse(argsText),
          });
        }}
      >
        <p>
          <label>
            Tool{" "}
            <input value={name} onChange={(event) => setName(event.target.value)} />
          </label>
        </p>
        <p>
          <label>
            Arguments JSON{" "}
            <input
              value={argsText}
              onChange={(event) => setArgsText(event.target.value)}
              size={40}
            />
          </label>
        </p>
        <button disabled={busy} type="submit">
          Call tool
        </button>
      </form>
      <pre>{log}</pre>
    </main>
  );
}
