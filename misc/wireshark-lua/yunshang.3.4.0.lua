--V3.4.0 2016-08-30
do
------bit operatopn
---------------------------------------------------------------------------------------------------
    bit = { data32 = {} }
    for i = 1,32 do
        bit.data32[i] = 2 ^ (32 - i)
    end

    function bit:d2b(arg)  --bit:d2b
        local tr = {}
        for i = 1,32 do
            if arg >= self.data32[i] then
                tr[i] = 1
                arg = arg - self.data32[i]
            else
                tr[i] = 0
            end
        end
        return tr
    end

    function bit:b2d(arg)  --bit:b2d
        local nr = 0
        for i = 1,32 do
            if arg[i] == 1 then
                nr = nr + 2 ^ (32 - i)
            end
        end
        return  nr
    end

    function bit:_xor(a, b)  --bit:xor
        local op1 = self:d2b(a)
        local op2 = self:d2b(b)
        local r = {}

        for i = 1,32 do
            if op1[i] == op2[i] then
                r[i] = 0
            else
                r[i] = 1
            end
        end
        return self:b2d(r)
    end

    function bit:_and(a, b)  --bit:_and
        local op1 = self:d2b(a)
        local op2 = self:d2b(b)
        local r={}

        for i = 1,32 do
            if op1[i] == 1 and op2[i] == 1  then
                r[i] = 1
            else
                r[i] = 0
            end
        end
        return  self:b2d(r)

    end

    function bit:_or(a, b)  --bit:_or
        local op1 = self:d2b(a)
        local op2 = self:d2b(b)
        local r = {}

        for i = 1,32 do
            if op1[i] == 1 or op2[i] == 1 then
                r[i] = 1
            else
                r[i] = 0
            end
        end
        return self:b2d(r)
    end

    function bit:_not(a)  --bit:_not
        local op1 = self:d2b(a)
        local r = {}

        for i = 1,32 do
            if op1[i] == 1 then
                r[i] = 0
            else
                r[i] = 1
            end
        end
        return self:b2d(r)
    end

    function bit:_rshift(a, n)  --bit:_rshift
        local op1 = self:d2b(a)
        local r = self:d2b(0)

        if n < 32 and n > 0 then
            for i = 1,n do
                for i = 31,1,-1 do
                    op1[i + 1] = op1[i]
                end
                op1[1] = 0
            end
            r = op1
        end
        return self:b2d(r)
    end

    function bit:_lshift(a,n)   --bit:_lshift
        local op1 = self:d2b(a)
        local r = self:d2b(0)

        if n < 32 and n > 0 then
            for i = 1,n do
                for i = 1,31 do
                    op1[i] = op1[i + 1]
                end
                op1[32] = 0
            end
            r = op1
        end
        return self:b2d(r)
    end

    function bit:print(ta)
        local sr = ""
        for i = 1,32 do
            sr = sr..ta[i]
        end
        print(sr)
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    C_DISTINGUISH_STUNv1  = 0x81
    C_DISTINGUISH_RRPCv1  = 0x91
    C_DISTINGUISH_PENEv1  = 0xA1
    C_DISTINGUISH_SUPPv1  = 0xB1
    C_DISTINGUISH_PUFFv1  = 0xC1
    C_DISTINGUISH_DCCPv1  = 0xD1

    C_STUN_QUERY_TYPE_REQ  = 1
    C_STUN_QUERY_TYPE_RSP  = 2
    C_STUN_NAT_UPDATE_REQ  = 3
    C_STUN_NAT_UPDATE_RSP  = 4
    C_STUN_NAT_QUIT        = 5

    C_RRPC_GENERAL_RSP     = 0
    C_RRPC_JOINLF_REQ      = 1
    C_RRPC_LEAVELF_REQ     = 2
    C_RRPC_INVESTIGATE_REQ = 20
    C_RRPC_INVESTIGATE_RSP = 21

    C_PENE_QUERYPEER_REQ   = 1
    C_PENE_QUERYPEER_RSP   = 2
    C_PENE_PENETRATE_REQ   = 3
    C_PENE_PENETRATE_RSP   = 4
    C_PENE_PENETRATE_ACK   = 5
    C_PENE_REVERSING_REQ   = 6
    C_PENE_KEEPALIVE_REQ   = 7

    C_SUPP_START_REQ    = 1
    C_SUPP_START_RSP    = 2
    C_SUPP_CHASE_REQ    = 3
    C_SUPP_CHASE_RSP    = 4
    C_SUPP_CHUNK_REQ    = 5
    C_SUPP_CHUNK_RSP    = 6
    C_SUPP_PIECE_DAT    = 7
    C_SUPP_ACK          = 8
    C_SUPP_FIN          = 9

    C_PUFF_SESSION_REQ  = 1
    C_PUFF_SESSION_RSP  = 2
    C_PUFF_SESSION_DAT  = 3
    C_PUFF_SESSION_HIB  = 4
    C_PUFF_SESSION_FIN  = 5

    C_DCCP_TYPE_SYNC    = 1
    C_DCCP_TYPE_SYNACK  = 2
    C_DCCP_TYPE_DATA    = 3
    C_DCCP_TYPE_ACK     = 4
    C_DCCP_TYPE_FIN     = 5

    C_CCCP_CHUNK_MAP_REQ      = 1
    C_CCCP_CHUNK_MAP_RSP      = 2
    C_CCCP_PULL_STREAM_REQ    = 3
    C_CCCP_PULL_STREAM_RSP    = 4
    C_CCCP_PULL_PIECE_REQ     = 5
    C_CCCP_PULL_PIECE_RSP     = 6
    C_CCCP_PULL_PIECE_DATA    = 7
    C_CCCP_PULL_PIECE_CANCEL  = 8
    C_CCCP_PULL_STREAM_FIN    = 9


    C_CCCP_PUSH_STREAM_REQ    = 20
    C_CCCP_PUSH_STREAM_RSP    = 21
    C_CCCP_PUSH_PIECE_DATA    = 22
    C_CCCP_PUSH_STREAM_FIN    = 23

---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------

    DMUX_Protocol = {
        [C_DISTINGUISH_STUNv1] = "STUNv1",
        [C_DISTINGUISH_RRPCv1] = "RRPCv1",
        [C_DISTINGUISH_PENEv1] = "PENEv1",
        [C_DISTINGUISH_SUPPv1] = "SUPPv1",
        [C_DISTINGUISH_PUFFv1] = "PUFFv1",
        [C_DISTINGUISH_DCCPv1] = "DCCPv1"
    }

    CCCP_Protocol = {
        [C_CCCP_CHUNK_MAP_REQ]      = "CHUNK_MAP_REQ",
        [C_CCCP_CHUNK_MAP_RSP]      = "CHUNK_MAP_RSP",
        [C_CCCP_PULL_STREAM_REQ]    = "PULL_STREAM_REQ",
        [C_CCCP_PULL_STREAM_RSP]    = "PULL_STREAM_RSP",
        [C_CCCP_PULL_PIECE_REQ]     = "PULL_PIECE_REQ",
        [C_CCCP_PULL_PIECE_RSP]     = "PULL_PIECE_RSP",
        [C_CCCP_PULL_PIECE_DATA]    = "PULL_PIECE_DATA",
        [C_CCCP_PULL_PIECE_CANCEL]  = "PULL_PIECE_CANCEL",
        [C_CCCP_PULL_STREAM_FIN]    = "PULL_STREAM_FIN",
        [C_CCCP_PUSH_STREAM_REQ]    = "PUSH_STREAM_REQ",
        [C_CCCP_PUSH_STREAM_RSP]    = "PUSH_STREAM_RSP",
        [C_CCCP_PUSH_PIECE_DATA]    = "PUSH_PIECE_DATA",
        [C_CCCP_PUSH_STREAM_FIN]    = "PUSH_STREAM_FIN"
    }

    DCCP_Protocol = {
        [C_DCCP_TYPE_SYNC] = "SYNC",
        [C_DCCP_TYPE_SYNACK] = "SYNACK",
        [C_DCCP_TYPE_DATA] = "DATA",
        [C_DCCP_TYPE_ACK] = "ACK",
        [C_DCCP_TYPE_FIN] = "FIN"
    }

    STUN_Protocol = {
        [C_STUN_QUERY_TYPE_REQ] = "QUERY_TYPE_REQ",
        [C_STUN_QUERY_TYPE_RSP] = "QUERY_TYPE_RSP",
        [C_STUN_NAT_UPDATE_REQ] = "NAT_UPDATE_REQ",
        [C_STUN_NAT_UPDATE_RSP] = "NAT_UPDATE_RSP",
        [C_STUN_NAT_QUIT] = "NAT_QUIT"
    }

    PENE_Protocol = {
        [C_PENE_QUERYPEER_REQ] = "QUERYPEER_REQ",
        [C_PENE_QUERYPEER_RSP] = "QUERYPEER_RSP",
        [C_PENE_PENETRATE_REQ] = "PENETRATE_REQ",
        [C_PENE_PENETRATE_RSP] = "PENETRATE_RSP",
        [C_PENE_PENETRATE_ACK] = "PENETRATE_ACK",
        [C_PENE_REVERSING_REQ] = "REVERSING_REQ",
        [C_PENE_KEEPALIVE_REQ] = "KEEPALIVE_REQ"
    }

    SUPP_Protocol = {
        [C_SUPP_START_REQ] = "START_REQ",
        [C_SUPP_START_RSP] = "START_RSP",
        [C_SUPP_CHASE_REQ] = "CHASE_REQ",
        [C_SUPP_CHASE_RSP] = "CHASE_RSP",
        [C_SUPP_CHUNK_REQ] = "CHUNK_REQ",
        [C_SUPP_CHUNK_RSP] = "CHUNK_RSP",
        [C_SUPP_PIECE_DAT] = "PIECE_DAT",
        [C_SUPP_ACK] = "ACK",
        [C_SUPP_FIN] = "FIN"
    }

    SUPP_Code = {
        [0] = "OK",
        [1] = "CONTINUE",
        [2] = "REDIRECT",
        [3] = "FUTURES",
        [4] = "OBSOLETE",
        [5] = "NOT_FOUND"
    }

    PUFF_Protocol = {
        [C_PUFF_SESSION_REQ] = "PUFF_SESSION_REQ",
        [C_PUFF_SESSION_RSP] = "PUFF_SESSION_RSP",
        [C_PUFF_SESSION_DAT] = "PUFF_SESSION_DAT",
        [C_PUFF_SESSION_HIB] = "PUFF_SESSION_HIB",
        [C_PUFF_SESSION_FIN] = "PUFF_SESSION_FIN"
    }

    PUFF_Code = {
        [0] = "OK",
        [1] = "Bad Request",
        [2] = "Server Busy",
        [3] = "Not Found",
        [4] = "No Response",
        [5] = "No Data"
    }

    RRPC_Protocol = {
        [C_RRPC_GENERAL_RSP] = "GENERAL_RSP",
        [C_RRPC_JOINLF_REQ] = "JOINLF_REQ",
        [C_RRPC_LEAVELF_REQ] = "LEAVELF_REQ",
        [C_RRPC_INVESTIGATE_REQ] = "INVESTIGATE_REQ",
        [C_RRPC_INVESTIGATE_RSP] = "INVESTIGATE_RSP"
    }

    NAT_TYPE = {
        [0] = "PUBLIC",
        [1] = "OPEN_OR_FULL_CONE",
        [2] = "IP_RESTRICTED",
        [3] = "IP_PORT_RESTRICTED",
        [4] = "SYMMETRIC_NAT",
        [5] = "UDP_BLOCKED",
        [6] = "UNKNOW"
    }
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local ysstun = Proto("YSSTUN", "Yunshang STUN Protocol")

    local f_pf_stun_ui4_reserved = ProtoField.uint8("Reserved", "Reserved", base.DEC, {[0] = "reserved"}, 0xF0)
    local f_pf_stun_ui4_Type = ProtoField.uint8("ysstun.type", "Type", base.DEC, STUN_Protocol, 0x0F)
    local f_pf_stun_ui8_Step = ProtoField.uint8("ysstun.step", "Step", base.DEC)
    local f_pf_stun_ui32_Pub_ip = ProtoField.ipv4("ysstun.pub_ip", "Pub_ip", base.DEC)
    local f_pf_stun_ui16_Pub_port = ProtoField.uint16("ysstun.pub_port", "Pub_port", base.DEC)
    local f_pf_stun_ui128_Peer_id = ProtoField.guid("ysstun.peer_id", "Peer_id", base.HEX)
    local f_pf_stun_ui8_Nat_type = ProtoField.uint8("ysstun.nat_type", "Nat_type",  base.DEC, NAT_TYPE)
    local f_pf_stun_ui32_Pri_ip = ProtoField.ipv4("ysstun.pri_ip", "Pri_ip", base.DEC)
    local f_pf_stun_ui16_Pri_port = ProtoField.uint16("ysstun.pri_port", "Pri_port", base.DEC)
    local f_pf_stun_ui8_code = ProtoField.uint8("ysstun.code", "code",  base.DEC)
    local f_pf_stun_ui64_timestamp = ProtoField.uint64("ysstun.timestamp", "timestamp",  base.DEC)

    ysstun.fields = {
        f_pf_stun_ui4_reserved,
        f_pf_stun_ui4_Type,
        f_pf_stun_ui8_Step,
        f_pf_stun_ui32_Pub_ip,
        f_pf_stun_ui16_Pub_port,
        f_pf_stun_ui128_Peer_id,
        f_pf_stun_ui8_Nat_type,
        f_pf_stun_ui32_Pri_ip,
        f_pf_stun_ui16_Pri_port,
        f_pf_stun_ui8_code,
        f_pf_stun_ui64_timestamp
    }

    local function ysstun_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        local stun_tree = tree:add(ysstun, buffer(0, L), "Yunshang STUN Protocol, "..STUN_Protocol[type])
        pinfo.cols.protocol:set("YSSTUN")
        pinfo.cols.info:set(" " .. STUN_Protocol[type])

        local offset = 0

---- Reserved and Type
        stun_tree:add(f_pf_stun_ui4_reserved, buffer(offset, 1), buffer(offset, 1):uint())
        stun_tree:add(f_pf_stun_ui4_Type, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1

        if type == C_STUN_QUERY_TYPE_REQ then --QUERY_TYPE_REQ
            stun_tree:add(f_pf_stun_ui8_Step, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end

        if type == C_STUN_QUERY_TYPE_RSP then --QUERY_TYPE_RSP
            stun_tree:add(f_pf_stun_ui8_Step, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            stun_tree:add(f_pf_stun_ui32_Pub_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            stun_tree:add(f_pf_stun_ui16_Pub_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end

        if type == C_STUN_NAT_UPDATE_REQ then --NAT_UPDATE_REQ
            stun_tree:add(f_pf_stun_ui128_Peer_id, buffer(offset, 16))
            offset = offset + 16
            stun_tree:add(f_pf_stun_ui8_Nat_type, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            stun_tree:add(f_pf_stun_ui32_Pri_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            stun_tree:add(f_pf_stun_ui16_Pri_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end

        if type == C_STUN_NAT_UPDATE_RSP then --NAT_UPDATE_RSP
            stun_tree:add(f_pf_stun_ui8_code, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            stun_tree:add(f_pf_stun_ui64_timestamp, buffer(offset, 8), buffer(offset, 8):uint64())
            offset = offset + 8
        end

        if type == C_STUN_NAT_QUIT then --NAT_QUIT
            stun_tree:add(f_pf_stun_ui128_Peer_id, buffer(offset, 16))
            offset = offset + 16
        end

        return true
    end

    local function ysstun_detector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        if type == C_STUN_QUERY_TYPE_REQ then ---- QUERY_TYPE_REQ ---- validator
            if L ~= 2 then return false end ---- 检查此类型包的长度
        elseif type == C_STUN_QUERY_TYPE_RSP then ---- QUERY_TYPE_RSP ---- validator
            if L ~= 8 then return false end ---- 检查此类型包的长度
        elseif type == C_STUN_NAT_UPDATE_REQ then ---- NAT_UPDATE_REQ ---- validator
            if L ~= 24 then return false end ---- 检查此类型包的长度
        elseif type == C_STUN_NAT_UPDATE_RSP then ---- NAT_UPDATE_RSP ---- validator
            if L ~= 10 then return false end ---- 检查此类型包的长度
        elseif type == C_STUN_NAT_QUIT then ---- NAT_QUIT ---- validator
            if L ~= 17 then return false end ---- 检查此类型包的长度
        else
            return false
        end
        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local yspene = Proto("YSPENE", "Yunshang PENE Protocol")

    local f_pf_pene_ui4_reserved = ProtoField.uint8("Reserved", "Reserved", base.DEC, {[0] = "reserved"}, 0xF0)
    local f_pf_pene_ui4_Type = ProtoField.uint8("yspene.type", "Type", base.DEC, PENE_Protocol, 0x0F)
    local f_pf_pene_ui8_Step = ProtoField.uint8("yspene.step", "Step", base.DEC)
    local f_pf_pene_ui32_Pub_ip = ProtoField.ipv4("yspene.pub_ip", "Pub_ip", base.DEC)
    local f_pf_pene_ui16_Pub_port = ProtoField.uint16("yspene.pub_port", "Pub_port", base.DEC)
    local f_pf_pene_ui128_Peer_id = ProtoField.guid("yspene.peer_id", "Dst_peer_id", base.HEX)
    local f_pf_pene_ui128_Dst_peer_id = ProtoField.guid("yspene.dst_peer_id", "Dst_peer_id", base.HEX)
    local f_pf_pene_ui128_Src_peer_id = ProtoField.guid("yspene.src_peer_id", "Src_peer_id", base.HEX)

    local f_pf_pene_ui8_Nat_type = ProtoField.uint8("yspene.nat_type", "Nat_type",  base.DEC, NAT_TYPE)
    local f_pf_pene_ui32_Pri_ip = ProtoField.ipv4("yspene.pri_ip", "Pri_ip", base.DEC)
    local f_pf_pene_ui16_Pri_port = ProtoField.uint16("yspene.pri_port", "Pri_port", base.DEC)

    local f_pf_pene_ui32_Src_public_ip = ProtoField.ipv4("yspene.src_public_ip", "Src_public_ip", base.DEC)
    local f_pf_pene_ui16_Src_public_port = ProtoField.uint16("yspene.src_public_port", "Src_public_port", base.DEC)

    local f_pf_pene_ui32_Stun_ip = ProtoField.ipv4("yspene.stun_ip", "Stun_ip", base.DEC)
    local f_pf_pene_ui16_Stun_port = ProtoField.uint16("yspene.stun_port", "Stun_port", base.DEC)

    local f_pf_pene_ui8_Transferred = ProtoField.uint8("yspene.transferred", "Transferred", base.DEC, {
            [0] = "false",
            [1] = "true"
        }
    )

    yspene.fields =  {
        f_pf_pene_ui4_reserved,
        f_pf_pene_ui4_Type,
        f_pf_pene_ui8_Step,
        f_pf_pene_ui32_Pub_ip,
        f_pf_pene_ui16_Pub_port,
        f_pf_pene_ui128_Peer_id,
        f_pf_pene_ui128_Dst_peer_id,
        f_pf_pene_ui128_Src_peer_id,
        f_pf_pene_ui8_Nat_type,
        f_pf_pene_ui32_Pri_ip,
        f_pf_pene_ui16_Pri_port,
        f_pf_pene_ui32_Src_public_ip,
        f_pf_pene_ui16_Src_public_port,
        f_pf_pene_ui32_Stun_ip,
        f_pf_pene_ui16_Stun_port,
        f_pf_pene_ui8_Transferred,
    }

    local function yspene_detector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        if type == C_PENE_QUERYPEER_REQ then ---- QUERYPEER_REQ ---- validator
            if L ~= 17 then return false end ---- 检查此类型包的长度
        elseif type == C_PENE_QUERYPEER_RSP then ---- QUERYPEER_RESP ---- validator
            if L ~= 30 then return false end ---- 检查此类型包的长度
        elseif type == C_PENE_PENETRATE_REQ then ---- PENETRATE_REQ ---- validator
            if L ~= 24 then return false end ---- 检查此类型包的长度
        elseif type == C_PENE_PENETRATE_RSP then ---- PENETRATE_RSP ---- validator
            if L ~= 17 then return false end ---- 检查此类型包的长度
        elseif type == C_PENE_PENETRATE_ACK then ---- PENETRATE_ACK ---- validator
            if L ~= 17 then return false end ---- 检查此类型包的长度
        elseif type == C_PENE_REVERSING_REQ then ---- REVERSING_REQ ---- validator
            if L ~= 45 then return false end ---- 检查此类型包的长度
        elseif type == C_PENE_KEEPALIVE_REQ then ---- KEEPALIVE_REQ ---- validator
            if L ~= 1 then return false end ---- 检查此类型包的长度
        else
            return false
        end
        return true
    end

    local function yspene_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        local pene_tree = tree:add(yspene, buffer(0, L), "Yunshang PENE Protocol, "..PENE_Protocol[type])

        local offset = 0
---- Reserved and Type
        pene_tree:add(f_pf_pene_ui4_reserved, buffer(offset, 1), buffer(offset, 1):uint())
        pene_tree:add(f_pf_pene_ui4_Type, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1

        if type == C_PENE_QUERYPEER_REQ then --QUERYPEER_REQ
            pene_tree:add(f_pf_pene_ui128_Peer_id, buffer(offset, 16))
            offset = offset + 16
        end

        if type == C_PENE_QUERYPEER_RSP then --QUERYPEER_RSP
            pene_tree:add(f_pf_pene_ui128_Peer_id, buffer(offset, 16))
            offset = offset + 16
            pene_tree:add(f_pf_pene_ui8_Nat_type, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            pene_tree:add(f_pf_pene_ui32_Pub_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            pene_tree:add(f_pf_pene_ui16_Pub_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            pene_tree:add(f_pf_pene_ui32_Pri_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            pene_tree:add(f_pf_pene_ui16_Pri_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end

        if type == C_PENE_PENETRATE_REQ then --PENETRATE_REQ
            pene_tree:add(f_pf_pene_ui128_Dst_peer_id, buffer(offset, 16))
            offset = offset + 16
            pene_tree:add(f_pf_pene_ui8_Transferred, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            pene_tree:add(f_pf_pene_ui32_Src_public_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            pene_tree:add(f_pf_pene_ui16_Src_public_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end

        if type == C_PENE_PENETRATE_RSP then --PENETRATE_RSP
            pene_tree:add(f_pf_pene_ui128_Src_peer_id, buffer(offset, 16))
            offset = offset + 16
        end

        if type == C_PENE_PENETRATE_ACK then --PENETRATE_ACK
            pene_tree:add(f_pf_pene_ui128_Src_peer_id, buffer(offset, 16))
            offset = offset + 16
        end

        if type == C_PENE_REVERSING_REQ then --REVERSING_REQ
            pene_tree:add(f_pf_pene_ui128_Dst_peer_id, buffer(offset, 16))
            offset = offset + 16
            pene_tree:add(f_pf_pene_ui128_Src_peer_id, buffer(offset, 16))
            offset = offset + 16
            pene_tree:add(f_pf_pene_ui32_Src_public_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            pene_tree:add(f_pf_pene_ui16_Src_public_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            pene_tree:add(f_pf_pene_ui32_Stun_ip, buffer(offset, 4), buffer(offset, 4):ipv4())
            offset = offset + 4
            pene_tree:add(f_pf_pene_ui16_Stun_port, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end

        if type == C_PENE_KEEPALIVE_REQ then --KEEPALIVE_REQ
        end


        pinfo.cols.protocol:set("YSPENE")
        pinfo.cols.info:set(" " .. PENE_Protocol[type])

        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local yssupp = Proto("YSSUPP", "Yunshang SUPP Protocol")

    local f_pf_supp_ui4_reserved = ProtoField.uint8("reserved", "reserved", base.DEC, {[0] = "RESERVED"}, 0xF0)
    local f_pf_supp_ui4_type = ProtoField.uint8("yssupp.type", "type", base.DEC, SUPP_Protocol, 0x0F)
    local f_pf_supp_ui16_channel_id = ProtoField.uint16("yssupp.channel_id", "channel_id", base.DEC)
    local f_pf_supp_ui16_sequence = ProtoField.uint16("yssupp.sequence", "sequence", base.DEC)
    local f_pf_supp_ui64_offset = ProtoField.uint64("yssupp.offset", "offset", base.DEC)
    local f_pf_supp_ui8_version_a = ProtoField.uint32("yssupp.versiona", "versiona", base.DEC, nil, 0xFF000000)
    local f_pf_supp_ui8_version_b = ProtoField.uint32("yssupp.versionb", "versionb", base.DEC, nil, 0x00FF0000)
    local f_pf_supp_ui16_version_c = ProtoField.uint32("yssupp.versionc", "versionc", base.DEC, nil, 0x0000FFFF)
    local f_pf_supp_ui128_url_md5 = ProtoField.guid("yssupp.url_md5", "url_md5", base.HEX)
    local f_pf_supp_ui16_max_recv_seq = ProtoField.uint16("yssupp.max_recv_seq", "max_recv_seq", base.DEC)
    local f_pf_supp_ui32_total_lost_pieces = ProtoField.uint32("yssupp.total_lost_pieces", "total_lost_pieces", base.DEC)
    local f_pf_supp_ui16_bitmap_len = ProtoField.uint16("yssupp.bitmap_len", "bitmap_len", base.DEC)
    local f_pf_supp_uix_file_url = ProtoField.stringz("yssupp.file_url", "file_url", base.DEC)
    local f_pf_supp_ui16_piece_size = ProtoField.uint16("yssupp.piece_size", "piece_size", base.DEC)
    local f_pf_supp_ui16_ppc = ProtoField.uint16("yssupp.ppc", "ppc", base.DEC)
    local f_pf_supp_ui16_cppc = ProtoField.uint16("yssupp.cppc", "cppc", base.DEC)
    local f_pf_supp_ui32_bitrate = ProtoField.uint32("yssupp.bitrate", "bitrate", base.DEC)
    local f_pf_supp_ui64_ioffset = ProtoField.uint64("yssupp.ioffset", "ioffset", base.DEC)
    local f_pf_supp_ui64_ielapse = ProtoField.uint64("yssupp.ielapse", "ielapse", base.DEC)
    local f_pf_supp_ui32_latest_chunk_id = ProtoField.uint32("yssupp.latest_chunk_id", "latest_chunk_id", base.DEC)
    local f_pf_supp_ui16_elapsed = ProtoField.uint16("yssupp.elapsed", "elapsed", base.DEC)
    local f_pf_supp_ui8_index = ProtoField.uint8("yssupp.index", "index", base.DEC)
    local f_pf_supp_ui8_total = ProtoField.uint8("yssupp.total", "total", base.DEC)
    local f_pf_supp_ui16_user_len = ProtoField.uint16("yssupp.user_len", "user_len", base.DEC)
    local f_pf_supp_ui8_code = ProtoField.uint8("yssupp.code", "code", base.DEC, SUPP_Code)
    local f_pf_supp_ui32_chunk_id = ProtoField.uint32("yssupp.chunk_id", "chunk_id", base.DEC)
    local f_pf_supp_ui8_piece_check = ProtoField.uint32("yssupp.piece_check", "piece_check", base.DEC, nil, 0xFF000000)
    local f_pf_supp_ui24_piece_index = ProtoField.uint32("yssupp.piece_index", "piece_index", base.DEC, nil, 0x00FFFFFF)
    local f_pf_supp_ui6912_piece_data = ProtoField.bytes("ui6912_piece_data", "piece_data", base.HEX)
    local f_pf_supp_uix_user_data = ProtoField.bytes("uix_user_data", "user_data", base.HEX)
    local f_pf_supp_uix_bitmap = ProtoField.bytes("uix_bitmap", "bitmap", base.HEX)

    yssupp.fields = {
        f_pf_supp_ui4_reserved,
        f_pf_supp_ui4_type,
        f_pf_supp_ui16_channel_id,
        f_pf_supp_ui16_sequence,
        f_pf_supp_ui64_offset,
        f_pf_supp_ui8_version_a,
        f_pf_supp_ui8_version_b,
        f_pf_supp_ui16_version_c,
        f_pf_supp_ui128_url_md5,
        f_pf_supp_ui16_max_recv_seq,
        f_pf_supp_ui32_total_lost_pieces,
        f_pf_supp_ui16_bitmap_len,
        f_pf_supp_uix_file_url,
        f_pf_supp_ui16_piece_size,
        f_pf_supp_ui16_ppc,
        f_pf_supp_ui16_cppc,
        f_pf_supp_ui32_bitrate,
        f_pf_supp_ui64_ioffset,
        f_pf_supp_ui64_ielapse,
        f_pf_supp_ui32_latest_chunk_id,
        f_pf_supp_ui16_elapsed,
        f_pf_supp_ui8_index,
        f_pf_supp_ui8_total,
        f_pf_supp_ui16_user_len,
        f_pf_supp_ui8_code,
        f_pf_supp_ui32_chunk_id,
        f_pf_supp_ui8_piece_check,
        f_pf_supp_ui24_piece_index,
        f_pf_supp_ui6912_piece_data,
        f_pf_supp_uix_user_data,
        f_pf_supp_uix_bitmap
    }

    local function yssupp_detector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)
        if type == C_SUPP_START_REQ then
            if L ~= 281 then return false end
        elseif type == C_SUPP_START_RSP then
            local user_len = buffer(31, 2):uint()
            if L ~= 33 + user_len then return false end
        elseif type == C_SUPP_CHASE_REQ then
            if L ~= 289 then return false end
        elseif type == C_SUPP_CHASE_RSP then
            local user_len = buffer(23, 2):uint()
            if L ~= 25 + user_len then return false end
        elseif type == C_SUPP_CHUNK_REQ then
            local bitmap_len = buffer(27, 2):uint()
            if L ~= 29 + bitmap_len then return false end
        elseif type == C_SUPP_CHUNK_RSP then
            local user_len = buffer(24, 2):uint()
            if L ~= 26 + user_len then return false end
        elseif type == C_SUPP_PIECE_DAT then
            if L ~= 877 then return false end
        elseif type == C_SUPP_ACK then
            if L ~= 29 then return false end
        elseif type == C_SUPP_FIN then
            if L ~= 19 then return false end
        end
        return true
    end


    local function yssupp_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        local supp_tree = tree:add(yssupp, buffer(0, L), "Yunshang SUPP Protocol, "..SUPP_Protocol[type])
        pinfo.cols.protocol:set("YSSUPP")
        pinfo.cols.info:set(" "..SUPP_Protocol[type])

        local offset = 0
---- Reserved and Type
        supp_tree:add(f_pf_supp_ui4_reserved, buffer(offset, 1), buffer(offset, 1):uint())
        supp_tree:add(f_pf_supp_ui4_type, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1
        supp_tree:add(f_pf_supp_ui16_channel_id, buffer(offset, 2), buffer(offset, 2):uint())
        offset = offset + 2

        if type == C_SUPP_START_REQ then
            supp_tree:add(f_pf_supp_ui16_sequence, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
            local url = buffer(offset, 256):string()
            supp_tree:add(f_pf_supp_uix_file_url, buffer(offset, 256))
            offset = offset + 256
            supp_tree:add(f_pf_supp_ui8_version_a, buffer(offset, 4))
            supp_tree:add(f_pf_supp_ui8_version_b, buffer(offset, 4))
            supp_tree:add(f_pf_supp_ui16_version_c, buffer(offset, 4))
            offset = offset + 4
            pinfo.cols.info:append(" "..url)
        end
        if type == C_SUPP_START_RSP then
            supp_tree:add(f_pf_supp_ui16_sequence, buffer(offset, 2))
            offset = offset + 2
            local ui8_code = buffer(offset, 1):uint()
            supp_tree:add(f_pf_supp_ui8_code, buffer(offset, 1))
            offset = offset + 1
            -- supp_tree:add(f_pf_supp_ui8_reserved, buffer(offset, 1))
            offset = offset + 1
            supp_tree:add(f_pf_supp_ui16_piece_size, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_ui16_ppc, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_ui32_bitrate, buffer(offset, 4))
            offset = offset + 4
            local ui64_iframe = buffer(offset, 8):uint64()
            supp_tree:add(f_pf_supp_ui64_ioffset, buffer(offset, 8))
            offset = offset + 8
            supp_tree:add(f_pf_supp_ui64_ielapse, buffer(offset, 8))
            offset = offset + 8
            local user_len = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_user_len, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_uix_user_data, buffer(offset, user_len))
            offset = offset + user_len
            pinfo.cols.info:append(" "..SUPP_Code[ui8_code].." I:"..ui64_iframe)
        end
        if type == C_SUPP_CHASE_REQ then
            supp_tree:add(f_pf_supp_ui16_sequence, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_ui64_offset, buffer(offset, 8))
            offset = offset + 8
            supp_tree:add(f_pf_supp_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
            local url = buffer(offset, 256):string()
            supp_tree:add(f_pf_supp_uix_file_url, buffer(offset, 256))
            offset = offset + 256
            supp_tree:add(f_pf_supp_ui8_version_a, buffer(offset, 4))
            supp_tree:add(f_pf_supp_ui8_version_b, buffer(offset, 4))
            supp_tree:add(f_pf_supp_ui16_version_c, buffer(offset, 4))
            offset = offset + 4
            pinfo.cols.info:append(" "..url)
        end
        if type == C_SUPP_CHASE_RSP then
            supp_tree:add(f_pf_supp_ui16_sequence, buffer(offset, 2))
            offset = offset + 2
            local ui8_code = buffer(offset, 1):uint()
            supp_tree:add(f_pf_supp_ui8_code, buffer(offset, 1))
            offset = offset + 1
            -- supp_tree:add(f_pf_supp_ui8_reserved, buffer(offset, 1))
            offset = offset + 1
            local ui64_iframe = buffer(offset, 8):uint64()
            supp_tree:add(f_pf_supp_ui64_ioffset, buffer(offset, 8))
            offset = offset + 8
            supp_tree:add(f_pf_supp_ui64_ielapse, buffer(offset, 8))
            offset = offset + 8
            local user_len = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_user_len, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_uix_user_data, buffer(offset, user_len))
            offset = offset + user_len
            pinfo.cols.info:append(" "..SUPP_Code[ui8_code].." I:"..ui64_iframe)
        end
        if type == C_SUPP_CHUNK_REQ then
            local ui32_chunk_id = buffer(offset, 4):uint()
            supp_tree:add(f_pf_supp_ui32_chunk_id, buffer(offset, 4))
            offset = offset + 4
            supp_tree:add(f_pf_supp_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
            supp_tree:add(f_pf_supp_ui8_version_a, buffer(offset, 4))
            supp_tree:add(f_pf_supp_ui8_version_b, buffer(offset, 4))
            supp_tree:add(f_pf_supp_ui16_version_c, buffer(offset, 4))
            offset = offset + 4
            local bitmap_len = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_bitmap_len, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_uix_bitmap, buffer(offset, bitmap_len))
            offset = offset + bitmap_len
            pinfo.cols.info:append(" cid:"..ui32_chunk_id)
        end
        if type == C_SUPP_CHUNK_RSP then
            local ui32_chunk_id = buffer(offset, 4):uint()
            supp_tree:add(f_pf_supp_ui32_chunk_id, buffer(offset, 4))
            offset = offset + 4
            local ui8_code = buffer(offset, 1):uint()
            supp_tree:add(f_pf_supp_ui8_code, buffer(offset, 1))
            offset = offset + 1
            supp_tree:add(f_pf_supp_ui64_ioffset, buffer(offset, 8))
            offset = offset + 8
            supp_tree:add(f_pf_supp_ui64_ielapse, buffer(offset, 8))
            offset = offset + 8
            local user_len = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_user_len, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_uix_user_data, buffer(offset, user_len))
            offset = offset + user_len
            pinfo.cols.info:append(" cid:"..ui32_chunk_id.." "..SUPP_Code[ui8_code])
        end

        if type == C_SUPP_PIECE_DAT then
            local ui16_sequence = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_sequence, buffer(offset, 2))
            offset = offset + 2
            local ui32_chunk_id = buffer(offset, 4):uint()
            supp_tree:add(f_pf_supp_ui32_chunk_id, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            local ui24_piece_index = bit:_and(buffer(offset, 4):uint(), 0xFFFFFF)
            supp_tree:add(f_pf_supp_ui8_piece_check, buffer(offset, 4), buffer(offset, 4):uint())
            supp_tree:add(f_pf_supp_ui24_piece_index, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            supp_tree:add(f_pf_supp_ui6912_piece_data, buffer(offset, 864))
            offset = offset + 864
            pinfo.cols.info:append(" cid:"..ui32_chunk_id.." pix:"..ui24_piece_index.." seq:"..ui16_sequence)
        end
        if type == C_SUPP_ACK then
            local cppc = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_cppc, buffer(offset, 2))
            offset = offset + 2
            supp_tree:add(f_pf_supp_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
            local max_recv_seq = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_max_recv_seq, buffer(offset, 2))
            offset = offset + 2
            local total_lost_pieces = buffer(offset, 4):uint()
            supp_tree:add(f_pf_supp_ui32_total_lost_pieces, buffer(offset, 4))
            offset = offset + 4
            local elapsed = buffer(offset, 2):uint()
            supp_tree:add(f_pf_supp_ui16_elapsed, buffer(offset, 2))
            offset = offset + 2
            pinfo.cols.info:append(" cppc:"..cppc.." seq:"..max_recv_seq.." lost:"..total_lost_pieces.." elapsed:"..elapsed)
        end
        if type == C_SUPP_FIN then
            supp_tree:add(f_pf_supp_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
        end

        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local yspuff = Proto("YSPUFF", "Yunshang PUFF Protocol")

    local f_pf_puff_ui4_reserved = ProtoField.uint8("reserved", "reserved", base.DEC, {[0] = "RESERVED"}, 0xF0)
    local f_pf_puff_ui4_type = ProtoField.uint8("yspuff.type", "type", base.DEC, PUFF_Protocol, 0x0F)
    local f_pf_puff_ui8_session_id = ProtoField.uint8("yspuff.session_id", "session_id", base.DEC)
    local f_pf_puff_ui128_peer_id = ProtoField.guid("yspuff.peer_id", "peer_id", base.HEX)
    local f_pf_puff_ui128_url_md5 = ProtoField.guid("yspuff.url_md5", "url_md5", base.HEX)
    local f_pf_puff_ui256_file_url = ProtoField.stringz("yspuff.file_url", "file_url", base.DEC)
    local f_pf_puff_ui16_cppc = ProtoField.uint16("yspuff.cppc", "cppc", base.DEC)
    local f_pf_puff_ui8_priority = ProtoField.uint8("yspuff.priority", "priority", base.DEC)
    local f_pf_puff_ui8_result = ProtoField.uint8("yspuff.result", "result", base.DEC, PUFF_Code)
    local f_pf_puff_ui32_chunk_id = ProtoField.uint32("yspuff.chunk_id", "chunk_id", base.DEC)
    local f_pf_puff_ui8_reason = ProtoField.uint8("yspuff.reason", "reason", base.DEC, PUFF_Code)
    local f_pf_puff_ui8_piece_check = ProtoField.uint32("yspuff.piece_check", "piece_check", base.DEC, nil, 0xFF000000)
    local f_pf_puff_ui24_piece_index = ProtoField.uint32("yspuff.piece_index", "piece_index", base.DEC, nil, 0x00FFFFFF)
    local f_pf_puff_ui6912_piece_data = ProtoField.bytes("ui6912_piece_data", "piece_data", base.HEX)

    yspuff.fields = {
        f_pf_puff_ui4_reserved,
        f_pf_puff_ui4_type,
        f_pf_puff_ui8_session_id,
        f_pf_puff_ui128_peer_id,
        f_pf_puff_ui128_url_md5,
        f_pf_puff_ui256_file_url,
        f_pf_puff_ui16_cppc,
        f_pf_puff_ui8_priority,
        f_pf_puff_ui8_result,
        f_pf_puff_ui32_chunk_id,
        f_pf_puff_ui8_reason,
        f_pf_puff_ui8_piece_check,
        f_pf_puff_ui24_piece_index,
        f_pf_puff_ui6912_piece_data
    }

    local function yspuff_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        local puff_tree = tree:add(yspuff, buffer(0, L), "Yunshang PUFF Protocol, "..PUFF_Protocol[type])
        pinfo.cols.protocol:set("YSPUFF")
        pinfo.cols.info:set(" " .. PUFF_Protocol[type])

        local offset = 0
---- Reserved and Type
        puff_tree:add(f_pf_puff_ui4_reserved, buffer(offset, 1), buffer(offset, 1):uint())
        puff_tree:add(f_pf_puff_ui4_type, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1
        puff_tree:add(f_pf_puff_ui8_session_id, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1

        if type == C_PUFF_SESSION_REQ then
            puff_tree:add(f_pf_puff_ui128_peer_id, buffer(offset, 16))
            offset = offset + 16
            puff_tree:add(f_pf_puff_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
            puff_tree:add(f_pf_puff_ui256_file_url, buffer(offset, 256))
            offset = offset + 256
            puff_tree:add(f_pf_puff_ui16_cppc, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            puff_tree:add(f_pf_puff_ui8_priority, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end
        if type == C_PUFF_SESSION_RSP then
            puff_tree:add(f_pf_puff_ui8_result, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end
        if type == C_PUFF_SESSION_DAT then
            local ui32_chunk_id = buffer(offset, 4):uint()
            puff_tree:add(f_pf_puff_ui32_chunk_id, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            local ui24_piece_index = bit:_and(buffer(offset, 4):uint(), 0xFFFFFF)
            puff_tree:add(f_pf_puff_ui8_piece_check, buffer(offset, 4), buffer(offset, 4):uint())
            puff_tree:add(f_pf_puff_ui24_piece_index, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            puff_tree:add(f_pf_puff_ui6912_piece_data, buffer(offset, 864))
            offset = offset + 864
            pinfo.cols.info:append(" cid:"..ui32_chunk_id.." pix:"..ui24_piece_index)
        end
        if type == C_PUFF_SESSION_HIB then
            puff_tree:add(f_pf_puff_ui128_peer_id, buffer(offset, 16))
            offset = offset + 16
            puff_tree:add(f_pf_puff_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
        end
        if type == C_PUFF_SESSION_FIN then
            puff_tree:add(f_pf_puff_ui128_peer_id, buffer(offset, 16))
            offset = offset + 16
            puff_tree:add(f_pf_puff_ui128_url_md5, buffer(offset, 16))
            offset = offset + 16
            puff_tree:add(f_pf_puff_ui8_reason, buffer(offset, 1):uint())
        end

        return true
    end

    local function yspuff_detector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)
        if type == C_PUFF_SESSION_REQ then
            if L ~= 293 then return false end
        elseif type == C_PUFF_SESSION_RSP then
            if L ~= 3 then return false end
        elseif type == C_PUFF_SESSION_DAT then
            if L ~= 874 and L ~= 874+8 then return false end
        elseif type == C_PUFF_SESSION_HIB then
            if L ~= 34 then return false end
        elseif type == C_PUFF_SESSION_FIN then
            if L ~= 35 then return false end
        end
        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local ysrrpc = Proto("YSRRPC", "Yunshang RRPC Protocol")

    local f_pf_rrpc_token = ProtoField.guid("ysrrpc.token", "token", base.HEX)
    local f_pf_rrpc_reserved = ProtoField.bytes("reserved", "reserved", base.DEC)
    local f_pf_rrpc_rrpc_id = ProtoField.uint16("ysrrpc.rrpc_id", "rrpc_id", base.DEC, RRPC_Protocol)
    local f_pf_rrpc_peer_id = ProtoField.guid("ysrrpc.peer_id", "peer_id", base.HEX)

    local f_pf_rrpc_result = ProtoField.uint8("ysrrpc.result", "result", base.DEC)

    local f_pf_rrpc_file_id = ProtoField.guid("ysrrpc.file_id", "file_id", base.HEX)
    local f_pf_rrpc_file_url = ProtoField.stringz("ysrrpc.file_url", "file_url", base.DEC)
    local f_pf_rrpc_piece_size = ProtoField.uint16("ysrrpc.piece_size", "piece_size", base.DEC)
    local f_pf_rrpc_ppc = ProtoField.uint16("ysrrpc.ppc", "ppc", base.DEC)
    local f_pf_rrpc_cppc = ProtoField.uint16("ysrrpc.cppc", "cppc", base.DEC)
    local f_pf_rrpc_push_server = ProtoField.stringz("ysrrpc.push_server", "push_server", base.DEC)
    local f_pf_rrpc_length = ProtoField.uint16("ysrrpc.length", "length", base.DEC)
    local f_pf_rrpc_request = ProtoField.stringz("ysrrpc.request", "request", base.DEC)
    local f_pf_rrpc_response = ProtoField.stringz("ysrrpc.response", "response", base.DEC)


    ysrrpc.fields = {
        f_pf_rrpc_token,
        f_pf_rrpc_reserved,
        f_pf_rrpc_rrpc_id,
        f_pf_rrpc_peer_id,
        f_pf_rrpc_result,
        f_pf_rrpc_file_id,
        f_pf_rrpc_file_url,
        f_pf_rrpc_piece_size,
        f_pf_rrpc_ppc,
        f_pf_rrpc_cppc,
        f_pf_rrpc_push_server,
        f_pf_rrpc_length,
        f_pf_rrpc_request,
        f_pf_rrpc_response
    }

    local function ysrrpc_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local rrpc_id = buffer(48, 2):uint()

        local rrpc_tree = tree:add(ysrrpc, buffer(0, L), "Yunshang RRPC Protocol, ".. RRPC_Protocol[rrpc_id])

        local offset = 0

        rrpc_tree:add(f_pf_rrpc_token, buffer(offset, 16))
        offset = offset + 16

        rrpc_tree:add(f_pf_rrpc_reserved, buffer(offset, 32))
        offset = offset + 32

        rrpc_tree:add(f_pf_rrpc_rrpc_id, buffer(offset, 2), rrpc_id)
        offset = offset + 2

        rrpc_tree:add(f_pf_rrpc_peer_id, buffer(offset, 16))
        offset = offset + 16

        if rrpc_id == C_RRPC_GENERAL_RSP then
            rrpc_tree:add(f_pf_rrpc_result, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end

        if rrpc_id == C_RRPC_JOINLF_REQ then
            rrpc_tree:add(f_pf_rrpc_file_id, buffer(offset ,16))
            offset = offset + 16
            rrpc_tree:add(f_pf_rrpc_file_url, buffer(offset, 256))
            offset = offset + 256
            rrpc_tree:add(f_pf_rrpc_piece_size, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            rrpc_tree:add(f_pf_rrpc_ppc, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            rrpc_tree:add(f_pf_rrpc_cppc, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            rrpc_tree:add(f_pf_rrpc_push_server, buffer(offset, 64))
            offset = offset + 64
        end

        if rrpc_id == C_RRPC_LEAVELF_REQ then
            rrpc_tree:add(f_pf_rrpc_file_id, buffer(offset, 16))
            offset = offset + 16
        end

        if rrpc_id == C_RRPC_INVESTIGATE_REQ then
            local ui16_length = buffer(offset, 2):uint();
            rrpc_tree:add(f_pf_rrpc_length, buffer(offset, 2))
            offset = offset + 2
            rrpc_tree:add(f_pf_rrpc_request, buffer(offset, ui16_length))
        end

        if rrpc_id == C_RRPC_INVESTIGATE_RSP then
            local ui16_length = buffer(offset, 2):uint();
            rrpc_tree:add(f_pf_rrpc_length, buffer(offset, 2))
            offset = offset + 2
            rrpc_tree:add(f_pf_rrpc_response, buffer(offset, ui16_length))
        end

        pinfo.cols.protocol:set("YSRRPC")
        pinfo.cols.info:set(" " .. RRPC_Protocol[rrpc_id])
        return true
    end

    local function ysrrpc_detector(buffer, pinfo, tree)
        local L = buffer:len()
        local rrpc_id = buffer(48, 2):uint()

        if rrpc_id == C_RRPC_GENERAL_RSP then
            if L ~= 67 then return false end
        elseif rrpc_id == C_RRPC_JOINLF_REQ then
            if L ~= 408 then return false end
        elseif rrpc_id == C_RRPC_LEAVELF_REQ then
            if L ~= 82 then return false end
        elseif rrpc_id == C_RRPC_INVESTIGATE_REQ then
            if L < 68 then return false end
        elseif rrpc_id == C_RRPC_INVESTIGATE_RSP then
            if L < 68 then return false end
        else
            return false
        end
        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local yscccp = Proto("YSCCCP", "Yunshang CCCP Protocol")

    local f_pf_cccp_ui8_type = ProtoField.uint8("yscccp.type", "type", base.DEC, CCCP_Protocol, 0x3F)
    local f_pf_cccp_ui16_request_id = ProtoField.uint16("yscccp.request_id", "request_id", base.DEC)
    local f_pf_cccp_ui128_peer_id = ProtoField.guid("yscccp.peer_id", "peer_id", base.HEX)
    local f_pf_cccp_ui128_file_id = ProtoField.guid("yscccp.file_id", "file_id", base.HEX)
    local f_pf_cccp_ui256_file_url = ProtoField.stringz("yscccp.file_url", "file_url", base.DEC)
    local f_pf_cccp_ui256_push_server = ProtoField.stringz("yscccp.push_server", "push_server", base.DEC)
    local f_pf_cccp_ui32_start_chunk_id = ProtoField.uint32("yscccp.start_chunk_id", "start_chunk_id", base.DEC)
    local f_pf_cccp_ui32_chunk_id = ProtoField.uint32("yscccp.chunk_id", "chunk_id", base.DEC)
    local f_pf_cccp_ui16_chunk_num = ProtoField.uint16("yscccp.chunk_num", "chunk_num", base.DEC)
    local f_pf_cccp_ui16_size = ProtoField.uint16("yscccp.size", "size", base.DEC)
    local f_pf_cccp_uixx_chunk_map = ProtoField.bytes("chunk_map", "chunk_map", base.HEX)
    local f_pf_cccp_ui8_priority = ProtoField.uint8("yscccp.priority", "priority", base.DEC)
    local f_pf_cccp_ui16_cppc = ProtoField.uint16("yscccp.cppc", "cppc", base.DEC)
    local f_pf_cccp_ui16_require_piece_num = ProtoField.uint16("yscccp.require_piece_num", "require_piece_num", base.DEC)
    local f_pf_cccp_ui8_status = ProtoField.uint8("yscccp.status", "status", base.DEC)
    local f_pf_cccp_ui8_accept_status = ProtoField.uint8("yscccp.accept_status", "accept_status", base.DEC, {
            [0] = "INITIAL",
            [1] = "PENDING",
            [2] = "ACCEPTED",
            [3] = "DECLINED"
        })
    local f_pf_cccp_ui16_accept_piece_num = ProtoField.uint16("yscccp.accept_piece_num", "accept_piece_num", base.DEC)
    local f_pf_cccp_ui8_piece_check = ProtoField.uint32("yscccp.piece_check", "piece_check", base.DEC, nil, 0xFF000000)
    local f_pf_cccp_ui24_piece_index = ProtoField.uint32("yscccp.piece_index", "piece_index", base.DEC, nil, 0x00FFFFFF)
    local f_pf_cccp_ui6912_piece_data = ProtoField.bytes("ui6912_piece_data", "piece_data", base.HEX)

    yscccp.fields = {
                        f_pf_cccp_ui8_type,
                        f_pf_cccp_ui16_request_id,
                        f_pf_cccp_ui128_peer_id,
                        f_pf_cccp_ui128_file_id,
                        f_pf_cccp_ui256_file_url,
                        f_pf_cccp_ui256_push_server,
                        f_pf_cccp_ui32_start_chunk_id,
                        f_pf_cccp_ui32_chunk_id,
                        f_pf_cccp_ui16_chunk_num,
                        f_pf_cccp_ui16_size,
                        f_pf_cccp_uixx_chunk_map,
                        f_pf_cccp_ui8_priority,
                        f_pf_cccp_ui16_cppc,
                        f_pf_cccp_ui16_require_piece_num,
                        f_pf_cccp_ui8_status,
                        f_pf_cccp_ui8_accept_status,
                        f_pf_cccp_ui16_accept_piece_num,
                        f_pf_cccp_ui8_piece_check,
                        f_pf_cccp_ui24_piece_index,
                        f_pf_cccp_ui6912_piece_data
                    }

    local function yscccp_detector(buffer, pinfo, tree)
        local L = buffer:len()
        if L < 2 then return false end
        local type = bit:_and(buffer(0, 1):uint(), 0x3F)

        if type == C_CCCP_CHUNK_MAP_REQ then
            if L < 24 then return false end
        elseif type == C_CCCP_CHUNK_MAP_RSP then
            if L < 8 then return false end
        elseif type == C_CCCP_PULL_STREAM_REQ then
            if L ~= 37 then return false end
        elseif type == C_CCCP_PULL_STREAM_RSP then
            if L ~= 4 then return false end
        elseif type == C_CCCP_PULL_PIECE_REQ then
            if L < 24 then return false end
        elseif type == C_CCCP_PULL_PIECE_RSP then
            if L < 4 then return false end
        elseif type == C_CCCP_PULL_PIECE_DATA then
            if L < 870 then return false end
        elseif type == C_CCCP_PULL_PIECE_CANCEL then
            if L < 2 then return false end
        elseif type == C_CCCP_PULL_STREAM_FIN then
            if L ~= 20 then return false end
        elseif type == C_CCCP_PUSH_STREAM_REQ then
            if L ~= 37 + 256 * 2 and L ~= 37 + 256 then return false end
        elseif type == C_CCCP_PUSH_STREAM_RSP then
            if L ~= 4 then return false end
        elseif type == C_CCCP_PUSH_PIECE_DATA then
            if L ~= 875 then return false end
        elseif type == C_CCCP_PUSH_STREAM_FIN then
            if L ~= 20 then return false end
        else
            return false
        end

        return true
    end

    local function yscccp_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x3F)

        local cccp_tree = tree:add(yscccp, buffer(0, L), "Yunshang CCCP Protocol, "..CCCP_Protocol[type])
        pinfo.cols.protocol:set("YSCCCP")
        pinfo.cols.info:append(", "..CCCP_Protocol[type])

        local offset = 0
        cccp_tree:add(f_pf_cccp_ui8_type, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1

        if type == C_CCCP_CHUNK_MAP_REQ then --CHUNK_MAP_REQ
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui128_file_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui32_start_chunk_id, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            cccp_tree:add(f_pf_cccp_ui16_chunk_num, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end
        if type == C_CCCP_CHUNK_MAP_RSP then --CHUNK_MAP_RSP
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui32_start_chunk_id, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            local ui16_size = buffer(offset, 2):uint()
            cccp_tree:add(f_pf_cccp_ui16_size, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_uixx_chunk_map, buffer(offset, ui16_size))
            offset = offset + ui16_size
        end
        if type == C_CCCP_PULL_STREAM_REQ then --PULL_STREAM_REQ
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui128_peer_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui128_file_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui16_cppc, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end
        if type == C_CCCP_PULL_STREAM_RSP then --PULL_STREAM_RSP
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui8_status, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end
        if type == C_CCCP_PULL_PIECE_REQ then --PULL_PIECE_REQ
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui128_file_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui32_chunk_id, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            cccp_tree:add(f_pf_cccp_ui8_priority, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            cccp_tree:add(f_pf_cccp_ui16_require_piece_num, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end
        if type == C_CCCP_PULL_PIECE_RSP then --PULL_PIECE_RSP
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui8_accept_status, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
            cccp_tree:add(f_pf_cccp_ui16_accept_piece_num, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end
        if type == C_CCCP_PULL_PIECE_DATA then --PULL_PIECE_DATA
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            local ui24_piece_index = bit:_and(buffer(offset, 4):uint(), 0xFFFFFF)
            cccp_tree:add(f_pf_cccp_ui8_piece_check, buffer(offset, 4), buffer(offset, 4):uint())
            cccp_tree:add(f_pf_cccp_ui24_piece_index, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            cccp_tree:add(f_pf_cccp_ui6912_piece_data, buffer(offset, 864))
            offset = offset + 864
            pinfo.cols.info:append(" pix:"..ui24_piece_index)
        end
        if type == C_CCCP_PULL_PIECE_CANCEL then --PULL_PIECE_CANCEL
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end
        if type == C_CCCP_PULL_STREAM_FIN then --PULL_STREAM_FIN
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui128_file_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui8_status, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end
        if type == C_CCCP_PUSH_STREAM_REQ then --PUSH_STREAM_REQ
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui128_peer_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui128_file_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui256_file_url, buffer(offset, 256))
            offset = offset + 256
            cccp_tree:add(f_pf_cccp_ui16_cppc, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
        end
        if type == C_CCCP_PUSH_STREAM_RSP then --PUSH_STREAM_RSP
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui8_status, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end
        if type == C_CCCP_PUSH_PIECE_DATA then --PUSH_PIECE_DATA
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            local ui32_chunk_id = buffer(offset, 4):uint();
            cccp_tree:add(f_pf_cccp_ui32_chunk_id, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            local ui24_piece_index = bit:_and(buffer(offset, 4):uint(), 0xFFFFFF)
            cccp_tree:add(f_pf_cccp_ui8_piece_check, buffer(offset, 4), buffer(offset, 4):uint())
            cccp_tree:add(f_pf_cccp_ui24_piece_index, buffer(offset, 4), buffer(offset, 4):uint())
            offset = offset + 4
            cccp_tree:add(f_pf_cccp_ui6912_piece_data, buffer(offset, 864))
            offset = offset + 864
            pinfo.cols.info:append(" cid:"..ui32_chunk_id.." pix:"..ui24_piece_index)
        end
        if type == C_CCCP_PUSH_STREAM_FIN then --PUSH_STREAM_FIN
            cccp_tree:add(f_pf_cccp_ui16_request_id, buffer(offset, 2), buffer(offset, 2):uint())
            offset = offset + 2
            cccp_tree:add(f_pf_cccp_ui128_file_id, buffer(offset, 16))
            offset = offset + 16
            cccp_tree:add(f_pf_cccp_ui8_status, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end

        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local ysdccp = Proto("YSDCCP", "Yunshang DCCP Protocol")

    local DCCP_Option = {
            [0] = "END",
            [1] = "Selective Ack",
            [2] = "ELAPSED"
    }
    local DCCP_Whyack = {
            [0] = "~~",
            [1] = "immediate acknowledge",
            [2] = "mis order",
            [3] = "delta delay",
            [4] = "lost detected",
            [5] = "timer"
    }

    local f_pf_dccp_ui1_opt = ProtoField.uint8("ysdccp.opt", "option", base.DEC, {
            [0] = "none",
            [1] = "have"
        }, 0x80
    )
    local f_pf_dccp_ui1_iack = ProtoField.uint8("ysdccp.iack", "immediate acknowledge", base.DEC, {
            [0] = "false",
            [1] = "true"
        }, 0x40
    )
    local f_pf_dccp_ui2_rsv = ProtoField.uint8("ui2_rsv", "reserved", base.DEC, nil, 0x30)
    local f_pf_dccp_ui4_type = ProtoField.uint8("ysdccp.type", "type", base.DEC, DCCP_Protocol, 0x0F)

    local f_pf_dccp_ui16_windowsize = ProtoField.uint32("ysdccp.windowsize", "windowsize", base.DEC)
    local f_pf_dccp_ui32_timestamp = ProtoField.uint32("ysdccp.timestamp", "timestamp", base.DEC)
    local f_pf_dccp_ui32_timedelay = ProtoField.uint32("ysdccp.timedelay", "timedelay", base.DEC)

    local f_pf_dccp_ui16_seqno = ProtoField.uint16("ysdccp.seqno", "seqno", base.DEC)
    local f_pf_dccp_ui16_ackno = ProtoField.uint16("ysdccp.ackno", "ackno", base.DEC)

    local f_pf_dccp_ui128_Peer_id = ProtoField.guid("ysdccp.peer_id", "peer_id", base.HEX)

    local f_dccp_ui8_ccid_a = ProtoField.uint24("ui8_ccid_a", "ccid", base.DEC, nil, 0xFF0000)
    local f_dccp_ui8_ccid_b = ProtoField.uint24("ui8_ccid_b", "ccid", base.DEC, nil, 0x00FF00)
    local f_dccp_ui8_ccid_c = ProtoField.uint24("ui8_ccid_c", "ccid", base.DEC, nil, 0x0000FF)

    local f_pf_dccp_ui8_whyack = ProtoField.uint8("ysdccp.whyack", "whyack", base.DEC, DCCP_Whyack)
    local f_pf_dccp_ui8_code = ProtoField.uint8("ysdccp.code", "code", base.DEC)

    local f_pf_dccp_ui4_opt_type = ProtoField.uint8("ui4_opt_type", "opt_type", base.DEC, DCCP_Option, 0xF0)
    local f_pf_dccp_ui4_opt_len = ProtoField.uint8("ui4_opt_len", "opt_len", base.DEC, nil, 0x0F)

    local f_dccp_ui8_opt_val = ProtoField.uint8("ui8_opt_val", "opt_val", base.DEC)
    local f_dccp_ui12_opt_val = ProtoField.uint16("ui12_opt_val", "opt_val", base.DEC, nil, 0x0FFF)
    local f_dccp_ui16_opt_val = ProtoField.uint16("ui16_opt_val", "opt_val", base.DEC)
    local f_dccp_ui24_opt_val = ProtoField.uint24("ui24_opt_val", "opt_val", base.DEC)
    local f_dccp_ui32_opt_val = ProtoField.uint32("ui32_opt_val", "opt_val", base.DEC)
    local f_dccp_ui64_opt_val = ProtoField.uint64("ui64_opt_val", "opt_val", base.DEC)
    local f_pf_dccp_uixx_opt_val = ProtoField.bytes("uixx_opt_val", "opt_val")

    local f_pf_dccp_data = ProtoField.bytes("payload", "payload", base.HEX)

    ysdccp.fields = {
                        f_pf_dccp_ui1_opt,
                        f_pf_dccp_ui1_iack,
                        f_pf_dccp_ui2_rsv,
                        f_pf_dccp_ui4_type,
                        f_pf_dccp_ui16_windowsize,
                        f_pf_dccp_ui32_timestamp,
                        f_pf_dccp_ui32_timedelay,
                        f_pf_dccp_ui16_seqno,
                        f_pf_dccp_ui16_ackno,
                        f_pf_dccp_ui128_Peer_id,
                        f_dccp_ui8_ccid_a,
                        f_dccp_ui8_ccid_b,
                        f_dccp_ui8_ccid_c,
                        f_pf_dccp_ui8_whyack,
                        f_pf_dccp_ui8_code,
                        f_pf_dccp_ui4_opt_type,
                        f_pf_dccp_ui4_opt_len,
                        f_dccp_ui8_opt_val,
                        f_dccp_ui12_opt_val,
                        f_dccp_ui16_opt_val,
                        f_dccp_ui24_opt_val,
                        f_dccp_ui32_opt_val,
                        f_dccp_ui64_opt_val,
                        f_pf_dccp_uixx_opt_val,
                        f_pf_dccp_data
                    }

    local function ysdccp_detector(buffer, pinfo, tree)
        local L = buffer:len()
        local opt = bit:_rshift(bit:_and(buffer(0, 1):uint(), 0x80), 7)
        local rsv = bit:_rshift(bit:_and(buffer(0, 1):uint(), 0x30), 4)
        local type = bit:_and(buffer(0, 1):uint(), 0x0F)

        if rsv ~= 0 then return false end

        if type == C_DCCP_TYPE_SYNC then
            if opt == 1 then return L > 31 else return L == 31 end
        elseif type == C_DCCP_TYPE_SYNACK then
            if opt == 1 then return L > 32 else return L == 32 end
        elseif type == C_DCCP_TYPE_DATA then
            if opt == 1 then return L > 15 else return L >= 15 end
        elseif type == C_DCCP_TYPE_ACK then
            if opt == 1 then return L > 16 else return L == 16 end
        elseif type == C_DCCP_TYPE_FIN then
            if opt == 1 then return L > 16 else return L == 16 end
        else
            return false
        end
    end

    local function ysdccp_dissector(buffer, pinfo, tree)
        local L = buffer:len()
        local type = bit:_and(buffer(0, 1):uint(), 0x0f)
        local opts = bit:_rshift(bit:_and(buffer(0, 1):uint(), 0x80), 7)

        local dccp_tree = tree:add(ysdccp, buffer(0, L), "Yunshang DCCP Protocol, "..DCCP_Protocol[type])

        local offset = 0
---- header
        dccp_tree:add(f_pf_dccp_ui1_opt, buffer(offset, 1), buffer(offset, 1):uint())
        dccp_tree:add(f_pf_dccp_ui1_iack, buffer(offset, 1), buffer(offset, 1):uint())
        dccp_tree:add(f_pf_dccp_ui2_rsv, buffer(offset, 1), buffer(offset, 1):uint())
        dccp_tree:add(f_pf_dccp_ui4_type, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1
        dccp_tree:add(f_pf_dccp_ui16_windowsize, buffer(offset, 2), buffer(offset, 2):uint())
        offset = offset + 2
        dccp_tree:add(f_pf_dccp_ui32_timestamp, buffer(offset, 4), buffer(offset, 4):uint())
        offset = offset + 4
        dccp_tree:add(f_pf_dccp_ui32_timedelay, buffer(offset, 4), buffer(offset, 4):uint())
        offset = offset + 4
        local ui16_seqno = buffer(offset, 2):uint();
        dccp_tree:add(f_pf_dccp_ui16_seqno, buffer(offset, 2), buffer(offset, 2):uint())
        offset = offset + 2
        local ui16_ackno = buffer(offset, 2):uint();
        dccp_tree:add(f_pf_dccp_ui16_ackno, buffer(offset, 2), buffer(offset, 2):uint())
        offset = offset + 2

        if type == C_DCCP_TYPE_SYNC then --SYNC
            dccp_tree:add(f_pf_dccp_ui128_Peer_id, buffer(offset, 16))
            offset = offset + 16
        end

        if type == C_DCCP_TYPE_SYNACK then --SYNACK
            dccp_tree:add(f_pf_dccp_ui128_Peer_id, buffer(offset, 16))
            offset = offset + 16
            dccp_tree:add(f_pf_dccp_ui8_code, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end

        if type == C_DCCP_TYPE_DATA then --DATA
        end

        if type == C_DCCP_TYPE_ACK then --ACK
            dccp_tree:add(f_pf_dccp_ui8_whyack, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end

        if type == C_DCCP_TYPE_FIN then --FIN
            dccp_tree:add(f_pf_dccp_ui8_code, buffer(offset, 1), buffer(offset, 1):uint())
            offset = offset + 1
        end

---- Handle Options

        local loop = 0
        while opts == 1 do
            loop = loop + 1
            local tl = buffer(offset, 1):uint()
            local ui4_opt_type = bit:_rshift(bit:_and(tl, 0xf0), 4)
            local ui4_opt_len = bit:_and(tl, 0x0f)

            local OptTree = dccp_tree:add(tostring(loop), buffer(offset, 1 + ui4_opt_len), "Option "..(DCCP_Option[ui4_opt_type] or tostring(ui4_opt_type)))

            if ui4_opt_type == 0 then ---- End
                OptTree:add(f_pf_dccp_ui4_opt_type, buffer(offset, 1), buffer(offset, 1):uint())
                offset = offset + 1
                break
            else
                OptTree:add(f_pf_dccp_ui4_opt_type, buffer(offset, 1), buffer(offset, 1):uint())
                OptTree:add(f_pf_dccp_ui4_opt_len, buffer(offset, 1), buffer(offset, 1):uint())
                offset = offset + 1
                OptTree:add(f_pf_dccp_uixx_opt_val, buffer(offset, ui4_opt_len))
                offset = offset + ui4_opt_len
            end
        end

        pinfo.cols.protocol:set("YSDCCP")
        pinfo.cols.info:set(""..DCCP_Protocol[type].." Seqno: "..ui16_seqno.."/"..ui16_ackno)

        if type == C_DCCP_TYPE_DATA then --DATA
            if yscccp_detector(buffer(offset):tvb(), pinfo, dccp_tree) then
                yscccp_dissector(buffer(offset):tvb(), pinfo, dccp_tree)
            else
                dccp_tree:add(f_pf_dccp_data, buffer(offset, L - offset))
            end
            offset = L
        end

        return true
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    local ys = Proto("YS", "Yunshang Protocol")

    local f_pf_ys_ui8_dmux = ProtoField.uint8("ys.demux", "demux type", base.HEX, DMUX_Protocol)

    ys.fields =  {
        f_pf_ys_ui8_dmux
    }

    local function ys_dissector(buffer, pinfo, tree, type)
        local L = buffer:len()

        local ys_tree = tree:add(ys, buffer(0, L), "Yunshang Protocol, "..DMUX_Protocol[type])

        local offset = 0
---- Dmux layer
        ys_tree:add(f_pf_ys_ui8_dmux, buffer(offset, 1), buffer(offset, 1):uint())
        offset = offset + 1

        -- pinfo.conversation = ys

        pinfo.cols.protocol:set("YS")
        pinfo.cols.info:set(" " .. DMUX_Protocol[type])

        if type == C_DISTINGUISH_STUNv1 then return ysstun_dissector(buffer(offset):tvb(), pinfo, ys_tree)
        elseif type == C_DISTINGUISH_RRPCv1 then return ysrrpc_dissector(buffer(offset):tvb(), pinfo, ys_tree)
        elseif type == C_DISTINGUISH_PENEv1 then return yspene_dissector(buffer(offset):tvb(), pinfo, ys_tree)
        elseif type == C_DISTINGUISH_SUPPv1 then return yssupp_dissector(buffer(offset):tvb(), pinfo, ys_tree)
        elseif type == C_DISTINGUISH_PUFFv1 then return yspuff_dissector(buffer(offset):tvb(), pinfo, ys_tree)
        elseif type == C_DISTINGUISH_DCCPv1 then return ysdccp_dissector(buffer(offset):tvb(), pinfo, ys_tree)
        else return false end
    end

    local function ys_detector(buffer, pinfo, tree)
        if buffer:len() < 2 then return false end
        local dmux = buffer(0, 1):uint()
        if dmux == C_DISTINGUISH_STUNv1 then if not ysstun_detector(buffer(1):tvb(), pinfo, tree) then return false end
        elseif dmux == C_DISTINGUISH_RRPCv1 then if not ysrrpc_detector(buffer(1):tvb(), pinfo, tree) then return false end
        elseif dmux == C_DISTINGUISH_PENEv1 then if not yspene_detector(buffer(1):tvb(), pinfo, tree) then return false end
        elseif dmux == C_DISTINGUISH_SUPPv1 then if not yssupp_detector(buffer(1):tvb(), pinfo, tree) then return false end
        elseif dmux == C_DISTINGUISH_PUFFv1 then if not yspuff_detector(buffer(1):tvb(), pinfo, tree) then return false end
        elseif dmux == C_DISTINGUISH_DCCPv1 then if not ysdccp_detector(buffer(1):tvb(), pinfo, tree) then return false end
        else return false end

        return ys_dissector(buffer, pinfo, tree, dmux)
    end
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
    ys:register_heuristic("udp", ys_detector)
end
