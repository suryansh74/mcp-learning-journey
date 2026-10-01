import "./globals.css";

export const metadata = {
  title: "MCP host",
  description: "Next.js host that calls a remote MCP server",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-stone-100 text-stone-900">{children}</body>
    </html>
  );
}
