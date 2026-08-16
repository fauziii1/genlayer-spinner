"""GenLayer TrustCheck - an Intelligent Contract for evidence-based claim review.

The contract asks validators to evaluate a claim against a supplied authoritative
source and returns a consensus label. This is a minimal reference implementation.
"""

from genlayer import gl, u256


class TrustCheck(gl.Contract):
    def __init__(self):
        self.claim = ""
        self.source_url = ""
        self.result = "UNSET"
        self.reason = ""

    @gl.public.write
    def submit_claim(self, claim: str, source_url: str):
        assert len(claim) > 5, "Claim is too short"
        assert source_url.startswith("http"), "A source URL is required"
        self.claim = claim
        self.source_url = source_url
        self.result = "PENDING"
        self.reason = "Awaiting Intelligent Contract consensus"

    @gl.public.write
    def evaluate(self):
        claim = self.claim
        source = self.source_url

        def evaluate_source() -> str:
            return gl.exec_prompt(
                f"""Evaluate this claim using the source URL.
Claim: {claim}
Source: {source}
Return exactly one label: VERIFIED, UNVERIFIED, or UNCERTAIN, followed by a concise reason.
Do not invent facts. If the source cannot substantiate the claim, use UNVERIFIED or UNCERTAIN."""
            )

        self.result = gl.eq_principle_strict(
            evaluate_source,
            lambda: "UNCERTAIN: insufficient authoritative evidence"
        )
        self.reason = "Consensus evaluation completed by GenLayer validators"

    @gl.public.view
    def get_result(self) -> dict:
        return {
            "claim": self.claim,
            "source_url": self.source_url,
            "result": self.result,
            "reason": self.reason,
        }
