"use client";

import { useState } from "react";

export default function Home() {
  const [tools, setTools] = useState([]);
  const [resources, setResources] = useState([]);
  const [log, setLog] = useState("Nothing called yet.");
  const [name, setName] = useState("say_hello");
  const [argsText, setArgsText] = useState('{"name":"Suryansh"}');
  const [uri, setUri] = useState("config://server");
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
      if (data.resources) setResources(data.resources);
    } catch (error) {
      setLog(String(error));
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <header className="mb-8">
        <p className="text-sm font-medium uppercase tracking-wide text-stone-500">
          MCP host
        </p>
        <h1 className="mt-1 text-3xl font-semibold">Remote server console</h1>
        <p className="mt-2 text-stone-600">
          The browser talks to this Next.js app. The app talks to{" "}
          <code className="rounded bg-stone-200 px-1">MCP_SERVER_URL</code>.
        </p>
      </header>

      <section className="mb-6 rounded-2xl border border-stone-200 bg-white p-5 shadow-sm">
        <div className="mb-3 flex items-center justify-between">
          <h2 className="text-lg font-medium">Tools</h2>
          <button
            className="rounded-lg bg-stone-900 px-3 py-1.5 text-sm text-white disabled:opacity-50"
            disabled={busy}
            onClick={() => callApi({ action: "list" })}
          >
            Refresh
          </button>
        </div>
        <ul className="space-y-2">
          {tools.map((tool) => (
            <li key={tool.name} className="flex items-start gap-3 text-sm">
              <button
                className="rounded-md border border-stone-300 px-2 py-1 font-mono text-xs"
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
              </button>
              <span className="text-stone-600">{tool.description}</span>
            </li>
          ))}
          {tools.length === 0 && (
            <li className="text-sm text-stone-500">Click Refresh to load tools.</li>
          )}
        </ul>
        <form
          className="mt-4 grid gap-3 border-t border-stone-100 pt-4"
          onSubmit={(event) => {
            event.preventDefault();
            callApi({
              action: "call",
              name,
              arguments: JSON.parse(argsText),
            });
          }}
        >
          <label className="text-sm">
            Tool
            <input
              className="mt-1 w-full rounded-lg border border-stone-300 px-3 py-2 font-mono text-sm"
              value={name}
              onChange={(event) => setName(event.target.value)}
            />
          </label>
          <label className="text-sm">
            Arguments JSON
            <input
              className="mt-1 w-full rounded-lg border border-stone-300 px-3 py-2 font-mono text-sm"
              value={argsText}
              onChange={(event) => setArgsText(event.target.value)}
            />
          </label>
          <button
            className="w-fit rounded-lg bg-amber-700 px-3 py-1.5 text-sm text-white disabled:opacity-50"
            disabled={busy}
            type="submit"
          >
            Call tool
          </button>
        </form>
      </section>

      <section className="mb-6 rounded-2xl border border-stone-200 bg-white p-5 shadow-sm">
        <div className="mb-3 flex items-center justify-between">
          <h2 className="text-lg font-medium">Resources</h2>
          <button
            className="rounded-lg bg-stone-900 px-3 py-1.5 text-sm text-white disabled:opacity-50"
            disabled={busy}
            onClick={() => callApi({ action: "resources" })}
          >
            List resources
          </button>
        </div>
        <ul className="mb-4 space-y-2">
          {resources.map((resource) => (
            <li key={resource.uri}>
              <button
                className="font-mono text-sm text-amber-800"
                onClick={() => setUri(resource.uri)}
              >
                {resource.uri}
              </button>
              <span className="ml-2 text-sm text-stone-500">{resource.name}</span>
            </li>
          ))}
        </ul>
        <form
          className="flex flex-wrap items-end gap-3"
          onSubmit={(event) => {
            event.preventDefault();
            callApi({ action: "read", uri });
          }}
        >
          <label className="min-w-64 flex-1 text-sm">
            URI
            <input
              className="mt-1 w-full rounded-lg border border-stone-300 px-3 py-2 font-mono text-sm"
              value={uri}
              onChange={(event) => setUri(event.target.value)}
            />
          </label>
          <button
            className="rounded-lg bg-amber-700 px-3 py-2 text-sm text-white disabled:opacity-50"
            disabled={busy}
            type="submit"
          >
            Read resource
          </button>
        </form>
      </section>

      <pre className="overflow-auto rounded-2xl bg-stone-900 p-4 text-sm text-stone-100">
        {log}
      </pre>
    </main>
  );
}
