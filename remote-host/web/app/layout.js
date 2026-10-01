export const metadata = {
  title: "MCP host",
  description: "Next.js host that calls a remote MCP server",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body style={{ fontFamily: "sans-serif", margin: "2rem", maxWidth: 720 }}>
        {children}
      </body>
    </html>
  );
}
