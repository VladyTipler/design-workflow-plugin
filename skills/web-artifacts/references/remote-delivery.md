# Optional remote delivery

Remote mode is opt-in. The project may name a provider/tool in .design-workflow.json, but the agent must use a real tool exposed by the current client; no adapter or endpoint is assumed.

1. Confirm that the user requested hosting and has reviewed the concrete local content, including any sensitive information.
2. Discover and inspect the tool schema and destination. Verify connector access with a harmless read. If access needs connection or approval, stop the remote step and keep local delivery available.
3. Upload only the agreed files. Use the tool's actual create/update contract. An update operation might change metadata only; do not assume it uploads file contents.
4. Report success only from the returned destination/link. On an ambiguous timeout, check existing state before retrying to avoid duplicate uploads.
5. Never automatically delete an artifact or infer a delete API. Existing destination replacement requires user authorization.

Secrets belong to the client's credential store, not the package or project JSON. No bundled MCP server, remote account or specific domain is required.
