from typing import Tuple

from ddht.constants import DISCOVERY_MAX_PACKET_SIZE

SESSION_IDLE_TIMEOUT = 60

ROUTING_TABLE_KEEP_ALIVE = 300

REQUEST_RESPONSE_TIMEOUT = 10

# safe upper bound on the size of the ENR list in a nodes message
FOUND_NODES_MAX_PAYLOAD_SIZE = DISCOVERY_MAX_PACKET_SIZE - 200


DEFAULT_BOOTNODES_ORIG: Tuple[str, ...] = (
    # DDHT: Alice
    "enr:-IS4QNIktXW8LPFA2B5n8jbF6fwScqUnO59gyZyg7CExFPHOO5z7nHBUjqbtbuS7Mk6Z2TL3eZiECpGmYCeGPlJzrLIDgmlkgnY0gmlwhC1PSnGJc2VjcDI1NmsxoQLvfEFi6FaFI7bp7Cw8yfZ17AdDwceRSQH7BxL5VhUNd4N1ZHCCdl8",  # noqa: E501
    # DDHT: Bob
    "enr:-IS4QKcAHi77_OQBuGolVX-I1dmQxyuZAsSTh3Z7Jck3LrzbYQ2NXzMEKvpit0cyH2coB55ddVDvKA8p5IUcg7DLQj4DgmlkgnY0gmlwhC1PW26Jc2VjcDI1NmsxoQPNz0D8sSVKyNTZuGRTTnPabutpJ8IUxpAyMqrVosZ14IN1ZHCCdl8",  # noqa: E501
    # CatDog: bridge bootnodes
    "enr:-Ku4QJmPsyq4lmDdFebMKXk7vdt8WsLWkArYT2K8eN057oFudm2tITrZJD9sq1x92-bRmXTyAJgb2FD4ior-KHIU3KcDh2F0dG5ldHOIAAAAAAAAAACEZXRoMpDaNQiCAAAAA___________gmlkgnY0gmlwhBK4vdCJc2VjcDI1NmsxoQMWAsR84_ETgq4-14FV2x00ptmI-YU3tdkZV9CUgYPEnIN1ZHCCI1s",  # noqa: E501
    # Lighthouse nodes
    "enr:-LK4QCGFeQXjpQkgOfLHsbTjD65IOtSqV7Qo-Qdqv6SrL8lqFY7INPMMGP5uGKkVDcJkeXimSeNeypaZV3MHkcJgr9QCh2F0dG5ldHOIAAAAAAAAAACEZXRoMpDnp11aAAAAAf__________gmlkgnY0gmlwhA37LMaJc2VjcDI1NmsxoQJ7k0mKtTd_kdEq251flOjD1HKpqgMmIETDoD-Msy_O-4N0Y3CCIyiDdWRwgiMo",  # noqa: E501
    "enr:-LK4QCpyWmMLYwC2umMJ_g0c9VY7YOFwZyaR80_tuQNTWOzJbaR82DDhVQYqmE_0gvN6Du5jwnxzIaaNRZQlVXzfIK0Dh2F0dG5ldHOIAAAAAAAAAACEZXRoMpDnp11aAAAAAf__________gmlkgnY0gmlwhCLR2xuJc2VjcDI1NmsxoQOYiWqrQtQksTEtS3qY6idxJE5wkm0t9wKqpzv2gCR21oN0Y3CCIyiDdWRwgiMo",  # noqa: E501
    # Prismatic
    "enr:-Ku4QHWezvidY_m0dWEwERrNrqjEQWrlIx7b8K4EIxGgTrLmUxHCZPW5-t8PsS8nFxAJ8k8YacKP5zPRk5gbsTSsRTQBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpAYrkzLAAAAAf__________gmlkgnY0gmlwhBLf22SJc2VjcDI1NmsxoQMypP_ODwTuBq2v0oIdjPGCEyu9Hb_jHDbuIX_iNvBRGoN1ZHCCGWQ",  # noqa: E501
    "enr:-Ku4QOnVSyvzS3VbF87J8MubaRuTyfPi6B67XQg6-5eAV_uILAhn9geTTQmfqDIOcIeAxWHUUajQp6lYniAXPWncp6UBh2F0dG5ldHOIAAAAAAAAAACEZXRoMpAYrkzLAAAAAf__________gmlkgnY0gmlwhBLf22SJc2VjcDI1NmsxoQKekYKqUtwbaJKKCct_srE5-g7tBUm68mj_jpeSb7CCqYN1ZHCCC7g",  # noqa: E501
)


DEFAULT_BOOTNODES: Tuple[str, ...] = (
    # 94.63.192.187:30303
    # "enr:-IS4QMKRqKacvGacwsChKkhY9OWyRAJvCkUG3mTlM-9DOtqcS7Zr7vVkf6s20ju6wCMNFE_ivWwYYp1CqA_ybJ9R_O8DgmlkgnY0gmlwhF4_wLuJc2VjcDI1NmsxoQLhZcNMi9TtZ9RxmjGNVG83YFyWQnyVdKr74_qXl7mbb4N1ZHCCdl8",  # noqa: E501
    # 192.168.1.112:30303
    "enr:-IS4QAVuwe64nAc-Lki-UHRUdpHzAB5xX_Uff0aQDBjIXgMlS7U7WjJ0h0Gja3-YTTTMTt6S5GG0doViOVYPMpYb2goDgmlkgnY0gmlwhMCoAXCJc2VjcDI1NmsxoQLhZcNMi9TtZ9RxmjGNVG83YFyWQnyVdKr74_qXl7mbb4N1ZHCCdl8",  # noqa: E501
)


PACKET_VERSION_1 = b"\x00\x01"

ID_NONCE_SIGNATURE_PREFIX = b"discovery v5 identity proof"

HEADER_PACKET_SIZE = 23

# PROTOCOL_ID = b"discv5"
# XXX: Must be the same length as "discv5"
PROTOCOL_ID = b"notdv5"

WHO_ARE_YOU_PACKET_SIZE = 24

HANDSHAKE_HEADER_PACKET_SIZE = 34

MESSAGE_PACKET_SIZE = 32
