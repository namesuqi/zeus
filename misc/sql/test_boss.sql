/*
Navicat MySQL Data Transfer

Source Server         : 10.6.3.4
Source Server Version : 50631
Source Host           : 10.6.3.4:3306
Source Database       : boss

Target Server Type    : MYSQL
Target Server Version : 50631
File Encoding         : 65001

Date: 2016-06-22 16:32:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ppc_auth_item
-- ----------------------------
DROP TABLE IF EXISTS `ppc_auth_item`;
CREATE TABLE `ppc_auth_item` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `tenant_id` int(10) unsigned NOT NULL COMMENT '平台租户id，即权限所属企业客户id',
  `name` varchar(64) NOT NULL COMMENT '权限名称',
  `type` int(11) NOT NULL,
  `description` text,
  `bizrule` text,
  `data` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='权限表';

-- ----------------------------
-- Records of ppc_auth_item
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_groups
-- ----------------------------
DROP TABLE IF EXISTS `ppc_groups`;
CREATE TABLE `ppc_groups` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户组id',
  `name` varchar(64) NOT NULL COMMENT '用户组名称',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_group_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='用户组';

-- ----------------------------
-- Records of ppc_groups
-- ----------------------------
INSERT INTO `ppc_groups` VALUES ('1', 'admin');
INSERT INTO `ppc_groups` VALUES ('3', 'customer');
INSERT INTO `ppc_groups` VALUES ('2', 'provider');

-- ----------------------------
-- Table structure for ppc_invitation
-- ----------------------------
DROP TABLE IF EXISTS `ppc_invitation`;
CREATE TABLE `ppc_invitation` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `invitation_code` char(32) NOT NULL COMMENT '邀请码',
  `promotion_rule_id` int(10) unsigned NOT NULL COMMENT '邀请码优惠规则',
  `from_tenant_id` int(10) unsigned NOT NULL COMMENT '邀请人所属的企业客户id',
  `from_user_id` bigint(20) unsigned NOT NULL COMMENT '邀请人的账号id',
  `current_use_times` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '当前使用次数',
  `max_use_times` int(10) unsigned NOT NULL DEFAULT '100' COMMENT '最大使用次数',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `bind_time` datetime DEFAULT NULL COMMENT '绑定时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_invitation_code` (`invitation_code`),
  KEY `index_from_tenant` (`from_tenant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='邀请码信息表';

-- ----------------------------
-- Records of ppc_invitation
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_push_address
-- ----------------------------
DROP TABLE IF EXISTS `ppc_push_address`;
CREATE TABLE `ppc_push_address` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `push_host` varchar(255) NOT NULL,
  `push_port` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_host_port` (`push_host`,`push_port`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='push-srv address, host and port';

-- ----------------------------
-- Records of ppc_push_address
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_role_auth
-- ----------------------------
DROP TABLE IF EXISTS `ppc_role_auth`;
CREATE TABLE `ppc_role_auth` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `item_id` int(10) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `bizrule` text,
  `data` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='角色权限映射表';

-- ----------------------------
-- Records of ppc_role_auth
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_roles
-- ----------------------------
DROP TABLE IF EXISTS `ppc_roles`;
CREATE TABLE `ppc_roles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `tenant_id` int(10) unsigned NOT NULL COMMENT '平台租户id，即角色所属企业客户id',
  `name` varchar(64) NOT NULL COMMENT '角色名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='角色表';

-- ----------------------------
-- Records of ppc_roles
-- ----------------------------
INSERT INTO `ppc_roles` VALUES ('1', '1', 'admin');

-- ----------------------------
-- Table structure for ppc_tenant_directory
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_directory`;
CREATE TABLE `ppc_tenant_directory` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tenant_id` int(10) unsigned NOT NULL COMMENT '平台租户id，即用户所属企业客户id',
  `dir_path` varchar(255) NOT NULL COMMENT '目录的完整路径',
  `parent` bigint(20) unsigned DEFAULT NULL COMMENT '该目录所在父目录',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_tenant_dir` (`tenant_id`,`dir_path`),
  KEY `index_parent_dir` (`parent`)
) ENGINE=InnoDB AUTO_INCREMENT=764 DEFAULT CHARSET=utf8 COMMENT='租户目录信息';

-- ----------------------------
-- Records of ppc_tenant_directory
-- ----------------------------
INSERT INTO `ppc_tenant_directory` VALUES ('1', '100000000', '/', null, '2015-09-01 01:06:16', null);
INSERT INTO `ppc_tenant_directory` VALUES ('2', '100000023', '/', null, '2015-09-01 01:06:16', null);
INSERT INTO `ppc_tenant_directory` VALUES ('3', '100000001', '/', null, '2015-09-01 01:06:16', null);
INSERT INTO `ppc_tenant_directory` VALUES ('347', '100000033', '/', null, '2016-02-18 20:45:08', null);
INSERT INTO `ppc_tenant_directory` VALUES ('581', '100000040', '/', null, '2016-03-11 10:29:11', null);
INSERT INTO `ppc_tenant_directory` VALUES ('612', '100000041', '/', null, '2016-04-05 16:53:19', null);

-- ----------------------------
-- Table structure for ppc_tenant_distribution
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_distribution`;
CREATE TABLE `ppc_tenant_distribution` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tenant_id` int(10) unsigned NOT NULL COMMENT '租户id',
  `distributor_id` int(10) unsigned NOT NULL COMMENT '分销商的租户id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_tenant_distributor` (`tenant_id`,`distributor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='分销关系表';

-- ----------------------------
-- Records of ppc_tenant_distribution
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_tenant_files
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_files`;
CREATE TABLE `ppc_tenant_files` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `sid` bigint(20) unsigned NOT NULL COMMENT '数据源id',
  `relative_url` varchar(1024) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `file_id` binary(16) NOT NULL,
  `md5` binary(16) DEFAULT '0000000000000000',
  `fsize` bigint(20) unsigned NOT NULL DEFAULT '0',
  `psize` smallint(5) unsigned NOT NULL DEFAULT '864',
  `ppc` smallint(5) unsigned NOT NULL DEFAULT '304',
  `type` smallint(5) unsigned NOT NULL DEFAULT '1' COMMENT '0:directory, 1: file',
  `state` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '0:sync unfinished, 1: not distributed, 2: distributed, 3: deleted',
  `is_public` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '0:token required on read; 1:publicly available',
  `dir_id` bigint(20) unsigned DEFAULT NULL COMMENT '该文件所在目录的id,若为空表示该文件未采用目录管理',
  `active_prefix_id` bigint(20) unsigned NOT NULL COMMENT '用户当初注册该文件时使用的prefix',
  `source` varchar(1024) DEFAULT NULL COMMENT 'source url',
  `ext` blob COMMENT 'Expand Information',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_dir` (`dir_id`),
  KEY `index_file` (`file_id`),
  KEY `index_md5` (`md5`)
) ENGINE=InnoDB AUTO_INCREMENT=270 DEFAULT CHARSET=utf8 COMMENT='租户注册和上传的文件';

-- ----------------------------
-- Records of ppc_tenant_files
-- ----------------------------
INSERT INTO `ppc_tenant_files` VALUES ('63', '5', '/media/new/2011/09/15/sd_dsj_hwdd01_201109115.ts', 0x343855B7C23B4C349AFFED0D3B5EC73D, 0x00000000000000000000000000000000, '252392068', '864', '304', '1', '2', '1', '2', '7', 'http://m.icntvcdn.com/media/new/2011/09/15/sd_dsj_hwdd01_201109115.ts', null, '2016-06-21 18:45:18', '2016-06-21 18:45:18');
INSERT INTO `ppc_tenant_files` VALUES ('86', '8', '/v-1/s-1/l-cn/r-1280x720/7.flv', 0x08ECD3F4050F4136A746E2B13CC57487, 0x00000000000000000000000000000000, '163027340', '864', '304', '1', '2', '1', '3', '9', 'http://ciwen.cloutropy.com/v-1/s-1/l-cn/r-1280x720/7.flv', null, '2016-06-22 10:55:57', '2016-06-22 10:55:57');
INSERT INTO `ppc_tenant_files` VALUES ('88', '8', '/v-1/s-1/l-cn/r-1280x720/3.flv', 0x642CC0FC311D47EE9DD61102E228B457, 0x00000000000000000000000000000000, '165065511', '864', '304', '1', '2', '1', '3', '9', 'http://ciwen.cloutropy.com/v-1/s-1/l-cn/r-1280x720/3.flv', null, '2016-06-22 10:58:06', '2016-06-22 10:58:06');
INSERT INTO `ppc_tenant_files` VALUES ('102', '9', '/05ee65b069f14744b8d411f45f520087', 0x05EE65B069F14744B8D411F45F520087, 0x00000000000000000000000000000000, '499118568', '864', '304', '1', '2', '1', '3', '9', 'http://buddiestv.qiniudn.com/sUWPWh5odxh9vtorJ2tsEue__hQ=/lqEfYNTpV7px5RAkIDOeZfr8BR0N', 0x7C270000789CAD5A4B8E55570CDCCB1B3FA9FDFF0C32080A83300082125082109334692991F83489587EECD3ECA06B03D6B9B6CB5576DDB76F2F37F7BFBD79F9E6CE3FFEF9EDAEFFFBFAF1CB33F97AFFF4DFDBF7EFEF7EF9E1E69FCF4F3FFCFEFCD74FAFF3D3377FF5E3DF3FFFF4E2F68F0F5FEAC92B7A7E737FFB175DAEEACD2DF5EEFAD858BCB12C3DE8F1B1E472B54E5597C7C7D2CB55DA8C0AF02E9B6F2CA63640BE7CDEE559D9F1F85871B90691B10362E5E5EA55AE06C8575DAE95CA85C8579FDC9720EAC8D3F8CE66A68006E3EDFC69315640F6F9B47EF39400106C7ADF382308116C9ADF06DD0C1916BED342A4210598F6172D2548CE72AB39BD2106083600309B6A420AD03BC9AA04326177F4977721AA298B80E8861440160134E110059045407B84207276C6BF3141723608B0A4CE044C0D190428EBCC20009C641020A14284C8599D3EB346D0892C07589320AAA90701F33044D32A6FCE520431CF7410201551886AEA2040D5660201E0A48B80413904E8BA1C403A08407CE62240C80DD1B49A074E9C84C8D922A0DDB4119F3908F0602B04A1D820603B3610D5B48380D046B0932D0226FD81108EB608A819DA01A8A60D025C68908E08360848CD60C86E12FB32B540C0C90601492383209FB96B00372BA49ABD390B5244D3FA2020C4DB104DEB838059756604215E261BAC1CA2CF7C77E059801DB16BFA2080452411CBB9EF16AC4A06D9A80F07283B82847D398066DB81041B0488090B2467BB07A49223E4412C07A4254420C77240693342D386AC708981006004853E90B020183D7613E6D16788D68845C0A81686DC8176131ED634C4D4887C781921E659AC0AA2643744010601E5C39C88A5220F02B28911C733DEEBD9CC2004367310E0233520D5CCE500C9A840045B04ECFD06A1B6F3DC822C20C7B81C049838054252E522C09D208C9ECB01C1AB9001C176139E85D32057DA45000F9E10D5ACE500094D44CE4ACE522186386CD77102A81271A72D5BAAE3791CE2331701A3A70AF299CB01250DB920571E46E780BC6C39C0BC13B188D5F1034A083169FBDC8276AD03BCAC8F1F40AA8879D6724E5E0D198EAD2758418663DBC38E0E392CF5E100DEDE00045B0EA0F082045B04901323266DD791EEE29002EC26CCA48918414C6B89D9903AE23B997825728D0C82445B4B60CA09911B93B135FFD420338DE9C040C23055F0C3EB1D0891C0F4000453C449886937E2A4208484673A500803F55BAFECAB863803BCF6B06825411CDDE30FCFD04D8871BA06B1CE5A96902A1C8778F81D72CEE4B5887DDA0DB2CBF27AC483D36E4C4DF73C3A8F0B845EE07589A53B145385631164434E1D7C7C625782A8495EA3D85B0DB203F13AC53EED8131C48F55CCA910DB93D72B1E095E90BF8E580E2F541042ECF2BAC552D3211064AD5D3C1D320D0279DBF73F861A715BE3358C87E8A520C85AC7388241937C2D6317DBD5F6DDFF89AA9DBD, '2016-06-22 11:58:15', '2016-06-22 11:58:15');

-- ----------------------------
-- Table structure for ppc_tenant_live_channel
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_live_channel`;
CREATE TABLE `ppc_tenant_live_channel` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tenant_name` varchar(64) NOT NULL COMMENT '�⻧���ƣ�����ҵ�ͻ�����',
  `channel_name` varchar(255) NOT NULL,
  `file_id` varchar(64) NOT NULL,
  `pull_url` varchar(1024) DEFAULT NULL,
  `push_url` varchar(1024) DEFAULT NULL,
  `output_url` varchar(1024) DEFAULT NULL,
  `mode` varchar(8) DEFAULT NULL COMMENT 'pull or push',
  `stream_rate` int(10) unsigned DEFAULT NULL COMMENT 'unit: b(bit)/s',
  `format` varchar(16) DEFAULT NULL COMMENT 'flv, ts or hls',
  `channel_status` varchar(32) DEFAULT NULL COMMENT 'ready run stop',
  `piece_data_size` int(10) unsigned DEFAULT NULL,
  `ppc` int(10) unsigned DEFAULT NULL,
  `begin_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_file_id` (`file_id`),
  KEY `index_tenant_name` (`tenant_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='�⻧ֱ��Ƶ��';

-- ----------------------------
-- Records of ppc_tenant_live_channel
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_tenant_peer_prefix
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_peer_prefix`;
CREATE TABLE `ppc_tenant_peer_prefix` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tenant_id` int(10) unsigned NOT NULL COMMENT '租户id',
  `peer_prefix` varchar(32) NOT NULL COMMENT '租户所对应的节点识别码前缀',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_peer_prefix` (`peer_prefix`),
  KEY `index_tenant` (`tenant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COMMENT='租户节点前缀关系表';

-- ----------------------------
-- Records of ppc_tenant_peer_prefix
-- ----------------------------
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('1', '100000000', '00000000');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('2', '100000001', '00010001');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('3', '100000002', '00010002');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('4', '100000003', '00010003');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('5', '100000004', '00010004');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('6', '100000005', '00010005');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('7', '100000006', '00010006');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('8', '100000007', '00010007');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('9', '100000008', '00010008');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('10', '100000009', '00010009');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('11', '100000010', '00000010');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('12', '100000011', '00010011');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('13', '100000012', '00010012');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('14', '100000013', '00010013');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('15', '100000014', '00010014');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('16', '100000015', '00010015');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('17', '100000016', '00010016');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('18', '100000017', '00010017');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('19', '100000018', '00010018');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('20', '100000019', '00010019');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('21', '100000020', '00010020');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('22', '100000021', '00010021');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('23', '100000022', '00010022');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('24', '100000023', '00010023');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('25', '100000024', '00010024');
INSERT INTO `ppc_tenant_peer_prefix` VALUES ('26', '100000025', '00010025');

-- ----------------------------
-- Table structure for ppc_tenant_source
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_source`;
CREATE TABLE `ppc_tenant_source` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tenant_id` bigint(20) NOT NULL COMMENT '用户id',
  `source_type` varchar(16) NOT NULL COMMENT '数据源类型，暂包括OSS、CDN和M3U8',
  `auto_register` tinyint(3) NOT NULL DEFAULT '0' COMMENT '自动注册为1，否则为0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_tenant_source` (`tenant_id`,`source_type`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COMMENT='租户资源类型关系表';

-- ----------------------------
-- Records of ppc_tenant_source
-- ----------------------------
INSERT INTO `ppc_tenant_source` VALUES ('1', '100000000', 'OSS', '0');
INSERT INTO `ppc_tenant_source` VALUES ('2', '100000000', 'CDN', '1');
INSERT INTO `ppc_tenant_source` VALUES ('3', '100000000', 'M3U8', '1');
INSERT INTO `ppc_tenant_source` VALUES ('4', '100000023', 'OSS', '0');
INSERT INTO `ppc_tenant_source` VALUES ('5', '100000023', 'CDN', '1');
INSERT INTO `ppc_tenant_source` VALUES ('6', '100000023', 'M3U8', '1');
INSERT INTO `ppc_tenant_source` VALUES ('7', '100000001', 'OSS', '0');
INSERT INTO `ppc_tenant_source` VALUES ('8', '100000001', 'CDN', '1');
INSERT INTO `ppc_tenant_source` VALUES ('9', '100000001', 'M3U8', '1');
INSERT INTO `ppc_tenant_source` VALUES ('10', '100000033', 'CDN', '1');
INSERT INTO `ppc_tenant_source` VALUES ('11', '100000040', 'CDN', '1');
INSERT INTO `ppc_tenant_source` VALUES ('12', '100000040', 'M3U8', '1');
INSERT INTO `ppc_tenant_source` VALUES ('13', '100000041', 'CDN', '1');
INSERT INTO `ppc_tenant_source` VALUES ('14', '100000041', 'M3U8', '1');

-- ----------------------------
-- Table structure for ppc_tenant_url_prefix
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenant_url_prefix`;
CREATE TABLE `ppc_tenant_url_prefix` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tenant_id` int(10) unsigned DEFAULT NULL COMMENT '租户id',
  `url_prefix` varchar(64) NOT NULL COMMENT '租户视频源前缀',
  `verify_code` varchar(32) DEFAULT NULL COMMENT '租户视频源验证码',
  `verify` tinyint(3) NOT NULL COMMENT '域名待审核为0，通过为1',
  PRIMARY KEY (`id`),
  KEY `index_url_prefix` (`url_prefix`),
  KEY `index_tenant` (`tenant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=218 DEFAULT CHARSET=utf8 COMMENT='租户视频源前缀关系表';

-- ----------------------------
-- Records of ppc_tenant_url_prefix
-- ----------------------------
INSERT INTO `ppc_tenant_url_prefix` VALUES ('1', null, 'cdn.cloutropy.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('2', '100000000', 'cdn.cloutropy.com/leigang_oss', '', '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('3', '100000000', 'cdn.cloutropy.com/leigang_cdn', '', '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('4', '100000000', 'cdn.cloutropy.com/leigang_m3u8', '', '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('6', '100000023', 'f03.vod01.icntvcdn.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('7', '100000023', 'm.icntvcdn.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('9', '100000001', 'ciwen.cloutropy.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('10', '100000001', 'buddiestv.qiniudn.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('49', '100000023', 't027.vod05.icntvcdn.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('191', '100000040', 'ahtelecom.cloutropy.com', null, '1');
INSERT INTO `ppc_tenant_url_prefix` VALUES ('217', '100000041', 'testvideo.cloutropy.com', null, '1');

-- ----------------------------
-- Table structure for ppc_tenants
-- ----------------------------
DROP TABLE IF EXISTS `ppc_tenants`;
CREATE TABLE `ppc_tenants` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '租户id，即企业客户id',
  `name` varchar(64) NOT NULL COMMENT '租户名称，即企业客户名称',
  `license_verify` tinyint(3) NOT NULL COMMENT '实名认证待审核为0，拒绝为1，接受为2',
  `license_sn` varchar(32) DEFAULT NULL COMMENT '租户证件号码，企业营业执照号码或个人身份证号码',
  `license_name` varchar(32) DEFAULT NULL COMMENT '租户证件名称，企业营业执照名称或个人身份证姓名',
  `license_file_id` char(32) DEFAULT NULL COMMENT '租户证件文件id，租户上传的实名证件文件',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=100000042 DEFAULT CHARSET=utf8 COMMENT='租户表';

-- ----------------------------
-- Records of ppc_tenants
-- ----------------------------
INSERT INTO `ppc_tenants` VALUES ('1', 'superagent', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000000', 'leigang', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000001', 'ciwen', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000023', 'icntv', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000026', 'wasu', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000033', 'thunder', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000040', 'ahtelecom', '2', null, null, null);
INSERT INTO `ppc_tenants` VALUES ('100000041', 'test', '2', null, null, null);

-- ----------------------------
-- Table structure for ppc_url_prefix_push_address
-- ----------------------------
DROP TABLE IF EXISTS `ppc_url_prefix_push_address`;
CREATE TABLE `ppc_url_prefix_push_address` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url_prefix_id` bigint(20) unsigned NOT NULL,
  `push_address_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_url_prefix_id` (`url_prefix_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='url prefix id mapping push address id';

-- ----------------------------
-- Records of ppc_url_prefix_push_address
-- ----------------------------

-- ----------------------------
-- Table structure for ppc_user_group
-- ----------------------------
DROP TABLE IF EXISTS `ppc_user_group`;
CREATE TABLE `ppc_user_group` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL COMMENT '用户ID',
  `group_id` int(10) unsigned NOT NULL COMMENT '用户组ID',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_user_group` (`user_id`,`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COMMENT='用户分组信息';

-- ----------------------------
-- Records of ppc_user_group
-- ----------------------------
INSERT INTO `ppc_user_group` VALUES ('1', '1', '1');
INSERT INTO `ppc_user_group` VALUES ('2', '100000000', '1');
INSERT INTO `ppc_user_group` VALUES ('4', '100000000', '2');
INSERT INTO `ppc_user_group` VALUES ('3', '100000000', '3');
INSERT INTO `ppc_user_group` VALUES ('5', '100000001', '3');
INSERT INTO `ppc_user_group` VALUES ('7', '100000023', '2');
INSERT INTO `ppc_user_group` VALUES ('6', '100000023', '3');
INSERT INTO `ppc_user_group` VALUES ('8', '100000026', '3');
INSERT INTO `ppc_user_group` VALUES ('9', '100000033', '3');
INSERT INTO `ppc_user_group` VALUES ('11', '100000040', '2');
INSERT INTO `ppc_user_group` VALUES ('10', '100000040', '3');
INSERT INTO `ppc_user_group` VALUES ('13', '100000041', '2');
INSERT INTO `ppc_user_group` VALUES ('12', '100000041', '3');

-- ----------------------------
-- Table structure for ppc_user_role
-- ----------------------------
DROP TABLE IF EXISTS `ppc_user_role`;
CREATE TABLE `ppc_user_role` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `user_id` bigint(20) unsigned NOT NULL COMMENT '用户id',
  `role_id` int(10) unsigned NOT NULL COMMENT '角色名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户角色映射表';

-- ----------------------------
-- Records of ppc_user_role
-- ----------------------------
INSERT INTO `ppc_user_role` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for ppc_users
-- ----------------------------
DROP TABLE IF EXISTS `ppc_users`;
CREATE TABLE `ppc_users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `tenant_id` int(10) unsigned NOT NULL COMMENT '平台租户id，即用户所属企业客户id',
  `username` varchar(64) NOT NULL COMMENT '用户名',
  `password` char(32) NOT NULL COMMENT '密码',
  `salt` char(24) NOT NULL COMMENT 'hash salt',
  `phone` varchar(16) NOT NULL COMMENT '手机号码',
  `email` varchar(64) NOT NULL COMMENT '邮箱',
  `verify_code` varchar(32) NOT NULL DEFAULT '' COMMENT '用户激活验证码',
  `create_time` datetime NOT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_username` (`username`),
  UNIQUE KEY `index_phone` (`phone`),
  UNIQUE KEY `index_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=100000042 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Records of ppc_users
-- ----------------------------
INSERT INTO `ppc_users` VALUES ('1', '1', 'yunshang', '5ab4e4391c8708bd3e073e16ddb92316', 'PSD7t+nVJng8pybjuA11Ww==', '13900000000', 'sa@cloutropy.com', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456', '2016-05-11 15:06:26', null);
INSERT INTO `ppc_users` VALUES ('100000000', '100000000', 'leigang', '6b98577a4ae59958c051a69dd9efcc54', '68f26948a578c3e40d95fa14', '13512345678', 'leigang@cloutropy.com', 'c10583e4359bfd9af0ebeaec2356bde0', '2016-05-11 15:06:34', '2016-05-11 15:06:34');
INSERT INTO `ppc_users` VALUES ('100000001', '100000001', 'ciwen', 'ee3594b1007c738bf0cc4f654be546f8', 'edc5d93869519594372789b9', '80000000001', '100000001@cloutropy.com', '48303b79832bd8cf984c8ad4a06d3ad0', '2016-05-11 15:06:34', '2016-05-11 15:06:34');
INSERT INTO `ppc_users` VALUES ('100000023', '100000023', 'icntv', '1bbd474465543f55a0898f4f5c57ca7e', 'b72d5d2be0d15e9fdb9503d8', '80000000023', '100000023@cloutropy.com', 'df63882c81b565dd7116cf350d0b5ef6', '2016-05-11 15:06:34', '2016-05-11 15:06:34');
INSERT INTO `ppc_users` VALUES ('100000026', '100000026', 'wasu', '5ab4e4391c8708bd3e073e16ddb92316', 'PSD7t+nVJng8pybjuA11Ww==', '80000000026', '100000026@cloutropy.com', 'f92e16fa9da1766f8b1205b549982237', '2016-05-11 15:06:34', '2016-05-11 15:06:34');
INSERT INTO `ppc_users` VALUES ('100000033', '100000033', 'thunder', '24f5cec5d7c9bab63ae7973164278fcb', '6c82e303b551ded0b338f1ee', '80000000033', '100000033@cloutropy.com', '5c7686c0284e0875b26de99c1008e998', '2016-05-11 15:06:34', '2016-05-11 15:06:34');
INSERT INTO `ppc_users` VALUES ('100000040', '100000040', 'ahtelecom', '3ec285f03af3f998625522319cc151c9', '54d140f2f9f81ad614501135', '80000000040', '100000040@cloutropy.com', '772cb8dad8a1e33686a01f22361220c0', '2016-05-11 15:06:34', '2016-05-11 15:06:34');
INSERT INTO `ppc_users` VALUES ('100000041', '100000041', 'test', 'bdeae68ea63331a243b7015c0d7e1b25', 'a7442dda3ad93c9a726597e4', '80000000041', '100000041@cloutropy.com', '098f6bcd4621d373cade4e832627b4f6', '2016-05-11 15:06:34', '2016-05-11 15:06:34');

-- ----------------------------
-- View structure for view_user_files
-- ----------------------------
DROP VIEW IF EXISTS `view_user_files`;
CREATE ALGORITHM=UNDEFINED DEFINER=`ppc`@`localhost` SQL SECURITY DEFINER VIEW `view_user_files` AS select `ppc_tenant_files`.`id` AS `id`,`ppc_tenant_files`.`sid` AS `sid`,`ppc_tenant_files`.`relative_url` AS `relative_url`,hex(`ppc_tenant_files`.`file_id`) AS `file_id`,hex(`ppc_tenant_files`.`md5`) AS `md5`,`ppc_tenant_files`.`fsize` AS `fsize`,`ppc_tenant_files`.`type` AS `type`,`ppc_tenant_files`.`state` AS `state`,`ppc_tenant_files`.`is_public` AS `is_public`,`ppc_tenant_files`.`dir_id` AS `dir_id`,`ppc_tenant_files`.`active_prefix_id` AS `active_prefix_id`,`ppc_tenant_files`.`source` AS `source`,`ppc_tenant_files`.`create_time` AS `create_time` from `ppc_tenant_files` ;
